"""Legacy wrapper-level GS-1290 acquisition experiment."""

import matplotlib.pyplot as plt

import sdacq
from sdacq_types import PD_USB01, CHANNEL_1

DEVICE_ID = 1
NUM_PIXELS = 1024


def main():
    channel_id = None

    try:
        sdacq.init_library(flags=0, device_type=PD_USB01, res=0)
        sdacq.open_operation_electrics_device_ex(
            init_flags=0,
            device_type=PD_USB01,
            ID=DEVICE_ID,
            ipaddress=0,
            authcode=0,
            )
        sdacq.initialize_operation_electronics(init_flags=0, ID=DEVICE_ID)

        channel_id = sdacq.alloc_raw_data()
        sdacq.para_set_mapping(channel_id, CHANNEL_1, DEVICE_ID)

        sdacq.para_set_integration_time(100.0, DEVICE_ID)
        sdacq.get_spectra(DEVICE_ID)

        y = sdacq.get_stored_raw_data(channel_id)
        print(y)
        plt.plot(y[:NUM_PIXELS])
        plt.show()

    finally:
        if channel_id is not None:
            sdacq.free_raw_data(channel_id)

        sdacq.deinit_operation_electronics(DEVICE_ID)
        sdacq.close_operation_electronics(DEVICE_ID)
        sdacq.uninit_library(0)


if __name__ == '__main__':
    main()
