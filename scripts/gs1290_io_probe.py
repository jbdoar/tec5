"""Interactive, bounded I/O characterization for a GS-1290/PD-USB01.

This tool changes DOUT levels. Disconnect anything that must not be actuated,
keep clear of moving mechanisms, and run it only while observing the hardware.
Initialization resets the digital outputs; every probe also returns its output
to level 0 in a finally block.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import time

from tec5 import load
from tec5.sdacq_types import PD_USB01


def ask(prompt: str) -> str:
    return input(prompt).strip()


def confirm(prompt: str) -> bool:
    return ask(f"{prompt} [y/N] ").lower() in {"y", "yes"}


def probe_output(api, device_id: int, output: int, pulse_seconds: float) -> dict:
    print(f"\nDOUT{output}: level 0 -> level 1 for {pulse_seconds:g}s -> level 0")
    if not confirm(f"Actuate DOUT{output} now?"):
        return {"tested": False}

    try:
        api.set_digital_output(output, 0, device_id)
        time.sleep(0.2)
        api.set_digital_output(output, 1, device_id)
        time.sleep(pulse_seconds)
    finally:
        api.set_digital_output(output, 0, device_id)

    function = ask(
        "Recognized function [shutter/nd_filter/trigger/none/unknown]: "
    ).lower() or "unknown"
    high_state = ask(
        "State while level was 1 [open/closed/in/out/high/low/unknown]: "
    ).lower() or "unknown"
    notes = ask("Notes (optional): ")
    return {
        "tested": True,
        "function": function,
        "high_state": high_state,
        "low_state": "unknown",
        "pulse_seconds": pulse_seconds,
        "notes": notes,
    }


def monitor_inputs(api, device_id: int, seconds: float, interval: float) -> dict:
    print(f"\nMonitoring DIN1-3 for {seconds:g}s. Apply only safe logic-level signals.")
    started = time.monotonic()
    previous = None
    events = []
    while time.monotonic() - started < seconds:
        levels = tuple(api.get_digital_input(n, device_id) for n in (1, 2, 3))
        if levels != previous:
            elapsed = time.monotonic() - started
            print(f"{elapsed:8.3f}s  DIN1={levels[0]} DIN2={levels[1]} DIN3={levels[2]}")
            events.append({"seconds": round(elapsed, 6), "levels": levels})
            previous = levels
        time.sleep(interval)
    return {"duration_seconds": seconds, "events": events}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dll", help="SDACQ64MP.dll or its directory")
    parser.add_argument("--device-id", type=int, default=1)
    parser.add_argument(
        "--outputs",
        type=int,
        nargs="+",
        choices=(1, 2, 3),
        default=(1, 2, 3),
        help="digital outputs to probe in order (for example: --outputs 1 2)",
    )
    parser.add_argument("--pulse-seconds", type=float, default=0.75)
    parser.add_argument("--monitor-inputs", type=float, metavar="SECONDS", default=0)
    parser.add_argument("--poll-interval", type=float, default=0.01)
    parser.add_argument("--output", type=Path, default=Path("gs1290_io_mapping.json"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.pulse_seconds <= 0 or args.pulse_seconds > 5:
        raise SystemExit("--pulse-seconds must be greater than 0 and at most 5")
    if args.poll_interval <= 0:
        raise SystemExit("--poll-interval must be positive")

    print(__doc__)
    if not confirm("Hardware is safe to actuate and you want to continue?"):
        print("Cancelled without loading or changing the hardware.")
        return 1

    report = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "device": "GS-1290/PD-USB01",
        "device_id": args.device_id,
        "digital_outputs": {},
    }
    api = load(args.dll)
    library_initialized = False
    device_open = False
    electronics_initialized = False

    try:
        api.init_library(device_type=PD_USB01)
        library_initialized = True
        api.open_operation_electronics_device_ex(PD_USB01, args.device_id)
        device_open = True
        api.initialize_operation_electronics(args.device_id)
        electronics_initialized = True

        initial_inputs = [api.get_digital_input(n, args.device_id) for n in (1, 2, 3)]
        report["initial_digital_inputs"] = initial_inputs
        print(f"Initial inputs: DIN1={initial_inputs[0]} DIN2={initial_inputs[1]} DIN3={initial_inputs[2]}")

        for output in args.outputs:
            report["digital_outputs"][str(output)] = probe_output(
                api, args.device_id, output, args.pulse_seconds
            )

        if args.monitor_inputs > 0:
            report["digital_input_monitor"] = monitor_inputs(
                api, args.device_id, args.monitor_inputs, args.poll_interval
            )
    finally:
        # Initialization establishes level 0 as the known baseline. Restore it
        # even if a prompt, sleep, or native call was interrupted.
        if electronics_initialized:
            for output in args.outputs:
                try:
                    api.set_digital_output(output, 0, args.device_id)
                except Exception as exc:
                    print(f"WARNING: could not restore DOUT{output}: {exc}")
            try:
                api.deinitialize_operation_electronics(args.device_id)
            except Exception as exc:
                print(f"WARNING: deinitialization failed: {exc}")
        if device_open:
            try:
                api.close_operation_electronics(args.device_id)
            except Exception as exc:
                print(f"WARNING: device close failed: {exc}")
        if library_initialized:
            try:
                api.uninit_library()
            except Exception as exc:
                print(f"WARNING: library uninitialization failed: {exc}")

    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
