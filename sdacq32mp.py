from ctypes import *
import os
from sdacq_bindings import *

class SDACQ():
    def __init__(self):
        pass

    def init_library(self, flags: int = 0, device_type: int, res: int = 0) -> int:
        """
        Initializes SDACQ32MP library, must be called once before calling any other functions in the library.
        """
        lFlags = c_long(flags)
        l_Devicetype = c_long(device_type)
        lRes = c_long(res)
        ret = _lib.SDACQMP_InitLibrary(lFlags, l_Devicetype, lRes)
        return int(ret)
        
    def uninit_library(self, res: int = 0) -> int:
        """
        Has to be called once after closing the last opened operating electronics as last SDACQMP function call in any application.
        """
        lRes = c_long(res)
        return _lib.SDACQMP_UnInitLibrary(lRes)

    def open_operation_electronics_device_ex(self, init_flags: int, device_type: int, ID: int, ip_address: int = 0, auth_code: int = 0) -> int:
        """
        l_initflags:
        Bit 0 = 1: suppresses errors during initialization
        Bit 1 = 1: don’t close interface if function fails,
        because of non-initialized data in EEPROMs,
        should be 0 otherwise
        Bit 3 = 1: suppress automatic configuration
        Other bits are reserved and must be 0.
        """
        l_initflags = c_long(init_flags)
        l_Devicetype = c_long(device_type)
        l_ID = c_long(ID)
        ul_IPAddress = c_ulong(ip_address)
        ul_AuthCode = c_ulong(auth_code)
        return _lib.SDACQMP_OpenOperationElectronicsDeviceEx(l_initflags, l_Devicetype, l_ID, ul_IPAddress, ul_AuthCode)

    def initialize_operation_electronics(self):
        """
        Function allocates memory for a specified interface, opens the kernel
mode device respectively initiates a connection to the device and
links it as interface number ‘l_ID’.
        """
        pass

    def deinitialize_operation_electronics(self):
        pass

    def close_operation_electronics(self):
        pass

    def para_set_sensor_work_mode(self):
        pass

    def para_set_integration_time(self):
        pass

    def para_set_integration_time_2(self):
        pass

    def para_set_integration_time_3(self):
        pass

    def para_set_integration_time_for_deleting(self):
        pass

    def para_set_average_number(self):
        pass

    def para_get_average_number_limit(self):
        pass

    def para_set_burst_number(self):
        pass

    def para_get_burst_number_limit(self):
        pass

    def para_set_hardware_flash_mode_2(self):
        pass

    def para_set_flash_polarity(self):
        pass

    def para_get_hardware_flash_mode(self):
        pass

    def para_set_ext_trigg_timeout(self):
        pass

    def para_set_dark_current_correction_mode(self):
        pass

    def para_set_shutter_polarity(self):
        pass

    def para_set_shutter_control_mode(self):
        pass

    def para_get_integration_time_limits(self):
        pass

    def para_set_spec_buffer(self):
        pass

    def para_set_roi_settings(self):
        pass

    def get_spectra(self):
        pass

    def get_spectra_ex(self):
        pass

    def get_dark_current(self):
        pass

    def get_dark_current_with_shutter(self):
        pass

    def get_buffered_spectra(self):
        pass

    def set_interface_active(self):
        pass

    def set_interface_inactive(self):
        pass

    def io_set_dig_output_1(self):
        pass

    def io_set_dig_output_2(self):
        pass

    def io_set_dig_output_3(self):
        pass

    def io_set_dig_outputs(self):
        pass

    
