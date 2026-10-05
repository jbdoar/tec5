import os
from pathlib import Path
import unittest
from unittest.mock import patch

from tec5 import SDACQError
from tec5.sdacq import DLL_NAME, SDACQLibrary, _candidate


class FakeFunction:
    def __init__(self, result=0, effect=None):
        self.result = result
        self.effect = effect
        self.calls = []

    def __call__(self, *args):
        self.calls.append(args)
        if self.effect:
            self.effect(*args)
        return self.result


class FakeDLL:
    def __init__(self):
        self.SDACQMP_InitLibrary = FakeFunction()
        self.SDACQMP_IOSetDigOutput2 = FakeFunction()
        self.SDACQMP_IOGetDigInput3 = FakeFunction(
            effect=lambda value, _device: setattr(value._obj, "value", 1)
        )
        self.SDACQMP_ParaSetIntegrationTime = FakeFunction(
            effect=lambda value, _device: setattr(value._obj, "value", 12.5)
        )


class CandidateTests(unittest.TestCase):
    def test_explicit_file_wins(self):
        with patch.dict(os.environ, {"TEC5_SDACQ_DLL": "ignored"}):
            self.assertEqual(_candidate("chosen.dll"), Path("chosen.dll"))

    def test_environment_directory(self):
        with patch.dict(os.environ, {"TEC5_SDACQ_DLL": "."}):
            self.assertEqual(_candidate(None), Path(".") / DLL_NAME)


class ConvenienceTests(unittest.TestCase):
    def test_init_marshals_values(self):
        dll = FakeDLL()
        api = SDACQLibrary(dll, "fake")
        api.init_library(device_type=6, flags=1, res=2)
        args = dll.SDACQMP_InitLibrary.calls[0]
        self.assertEqual([value.value for value in args], [1, 6, 2])

    def test_in_out_value_is_returned(self):
        api = SDACQLibrary(FakeDLL(), "fake")
        self.assertEqual(api.set_integration_time(10, 1), 12.5)

    def test_nonzero_status_raises_with_context(self):
        dll = FakeDLL()
        dll.SDACQMP_InitLibrary.result = -1
        api = SDACQLibrary(dll, "fake")
        with self.assertRaises(SDACQError) as caught:
            api.init_library(device_type=6)
        self.assertEqual(caught.exception.function, "SDACQMP_InitLibrary")
        self.assertEqual(caught.exception.code, -1)

    def test_data_length_must_be_explicit_and_positive(self):
        with self.assertRaises(ValueError):
            SDACQLibrary(FakeDLL(), "fake").get_stored_raw_data(1, 0)

    def test_digital_output_is_selected_by_number(self):
        dll = FakeDLL()
        SDACQLibrary(dll, "fake").set_digital_output(2, True, 1)
        args = dll.SDACQMP_IOSetDigOutput2.calls[0]
        self.assertEqual([value.value for value in args], [1, 1])

    def test_digital_input_value_is_returned(self):
        api = SDACQLibrary(FakeDLL(), "fake")
        self.assertEqual(api.get_digital_input(3, 1), 1)

    def test_digital_channel_range_is_checked(self):
        api = SDACQLibrary(FakeDLL(), "fake")
        with self.assertRaises(ValueError):
            api.set_digital_output(4, 0, 1)


if __name__ == "__main__":
    unittest.main()


class FakeEEPROM:
    """The customer data area: 64 bytes, read and written 8 at most a call."""

    def __init__(self, broken=False):
        self.memory = bytearray(64)
        self.broken, self.calls = broken, []

    def read(self, family, res, buffer, index, count, device):
        self.calls.append(("read", family.value, index.value, count.value))
        assert count.value <= 8
        for k in range(count.value):
            buffer[k] = self.memory[index.value + k]
        return 0

    def write(self, family, res, buffer, index, count, device):
        self.calls.append(("write", family.value, index.value, count.value))
        assert count.value <= 8
        for k in range(count.value):
            self.memory[index.value + k] = buffer[k] ^ (0xFF if self.broken else 0)
        return 0


class CustomerDataTests(unittest.TestCase):
    def api(self, **kwargs):
        eeprom = FakeEEPROM(**kwargs)
        dll = FakeDLL()
        dll.SDACQMP_I2C_Read_EEPROM_CustData = eeprom.read
        dll.SDACQMP_I2C_Write_EEPROM_CustData = eeprom.write
        return SDACQLibrary(dll, "fake"), eeprom

    def test_written_in_chunks_of_8_and_read_back(self):
        api, eeprom = self.api()
        api.write_customer_data(b"GSRD\x01RADOMA-0123", 1, index=3)
        self.assertEqual(api.read_customer_data(1, index=3, count=16), b"GSRD\x01RADOMA-0123")
        writes = [c for c in eeprom.calls if c[0] == "write"]
        self.assertEqual([(c[2], c[3]) for c in writes], [(3, 8), (11, 8)])

    def test_a_write_that_doesnt_read_back_raises(self):
        api, _ = self.api(broken=True)
        with self.assertRaises(SDACQError):
            api.write_customer_data(b"abc", 1)

    def test_the_area_is_64_bytes(self):
        api, _ = self.api()
        with self.assertRaises(ValueError):
            api.write_customer_data(b"x" * 10, 1, index=60)
        self.assertEqual(len(api.read_customer_data(1)), 64)
