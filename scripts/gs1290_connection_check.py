"""Non-actuating connectivity check for a GS-1290/PD-USB01."""

from __future__ import annotations

import argparse
import json

from tec5 import load
from tec5.sdacq_types import PD_USB01


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dll", help="SDACQ64MP.dll or its directory")
    parser.add_argument("--device-id", type=int, default=1)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    api = load(args.dll)
    library_initialized = False
    device_open = False
    electronics_initialized = False
    cleanup_errors = []

    try:
        print(f"Loaded {api.path}")
        api.init_library(device_type=PD_USB01)
        library_initialized = True
        print("Library initialized")

        api.open_operation_electronics_device_ex(PD_USB01, args.device_id)
        device_open = True
        print(f"Device {args.device_id} opened")

        api.initialize_operation_electronics(args.device_id)
        electronics_initialized = True
        print("Operating electronics initialized")

        inputs = {
            f"DIN{number}": api.get_digital_input(number, args.device_id)
            for number in (1, 2, 3)
        }
        print("Digital inputs: " + json.dumps(inputs, sort_keys=True))
    finally:
        if electronics_initialized:
            try:
                api.deinitialize_operation_electronics(args.device_id)
                print("Operating electronics deinitialized")
            except Exception as exc:
                cleanup_errors.append(f"deinitialize: {exc}")
        if device_open:
            try:
                api.close_operation_electronics(args.device_id)
                print("Device closed")
            except Exception as exc:
                cleanup_errors.append(f"close: {exc}")
        if library_initialized:
            try:
                api.uninit_library()
                print("Library uninitialized")
            except Exception as exc:
                cleanup_errors.append(f"uninitialize: {exc}")

        for error in cleanup_errors:
            print(f"WARNING: cleanup failed: {error}")

    if cleanup_errors:
        return 2
    print("Connection check passed; no outputs were changed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
