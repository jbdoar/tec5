# tec5

Thin Python bindings for the Windows-only tec5 SDACQ64MP spectral acquisition
API.

The library aims to expose the complete vendor API without imposing behavior
specific to one instrument. A small set of Python-friendly methods covers the
acquisition path validated with a GS-1290 and PD-USB01. All registered native
entry points remain accessible for direct `ctypes` use.

## Project status

This project is under active development and is not yet a stable release.

- The core GS-1290 acquisition sequence has been exercised on real hardware.
- All functions in the repository's vendor API list are registered.
- APIs outside the validated acquisition path have not necessarily been tested
  with their corresponding hardware.
- Native signatures should ultimately be audited against the C headers from the
  exact installed SDK version.

The source currently targets 64-bit Windows and Python 3.12 or newer.

## Vendor software

The Python package does not currently distribute the tec5 DLLs or device
drivers. Install the appropriate tec5 software separately and provide either
the path to `SDACQ64MP.dll` or the directory containing it.

Companion libraries such as `SDPROCCL64.dll` should remain beside
`SDACQ64MP.dll`. Ethernet configurations may also require `PDETH64.dll`.

## Installation

For development, install the repository in editable mode:

```powershell
py -m pip install -e .
```

Locally retained vendor runtime files may be placed in the ignored
`.local/tec-runtime/` directory. Point the loader at it for the current shell:

```powershell
$env:TEC5_SDACQ_DLL = ".local\tec-runtime"
```

The project can also be built as a normal wheel:

```powershell
py -m pip wheel . --no-deps
```

## Loading the API

Pass the DLL or its containing directory explicitly:

```python
from tec5 import load

api = load(r"C:\Program Files\tec5\SDACQ64MP.dll")
# A directory works too:
# api = load(r"C:\Program Files\tec5")
```

Alternatively, set `TEC5_SDACQ_DLL` to either location:

```powershell
$env:TEC5_SDACQ_DLL = "C:\Program Files\tec5"
```

```python
from tec5 import load

api = load()
```

If neither is supplied, the library asks Windows to find `SDACQ64MP.dll`
through its normal DLL search mechanism.

## Basic acquisition

The following shows the low-level lifecycle. Applications must clean up every
resource they successfully acquire.

```python
from tec5 import load
from tec5.sdacq_types import CHANNEL_1, PD_USB01

DEVICE_ID = 1
PIXEL_COUNT = 1024  # Obtain this from the actual hardware configuration.

api = load(r"C:\path\to\tec5")
library_initialized = False
device_open = False
electronics_initialized = False
channel_id = None

try:
    api.init_library(device_type=PD_USB01)
    library_initialized = True

    api.open_operation_electronics_device_ex(PD_USB01, DEVICE_ID)
    device_open = True

    api.initialize_operation_electronics(DEVICE_ID)
    electronics_initialized = True

    channel_id = api.allocate_raw_data()
    api.set_mapping(channel_id, CHANNEL_1, DEVICE_ID)

    accepted_time = api.set_integration_time(100.0, DEVICE_ID)
    api.get_dark_current(DEVICE_ID)
    api.get_spectra(DEVICE_ID)
    spectrum = api.get_stored_raw_data(channel_id, PIXEL_COUNT)
finally:
    if channel_id is not None:
        api.free_raw_data(channel_id)
    if electronics_initialized:
        api.deinitialize_operation_electronics(DEVICE_ID)
    if device_open:
        api.close_operation_electronics(DEVICE_ID)
    if library_initialized:
        api.uninit_library()
```

`pixel_count` is intentionally explicit. The native copy function does not
receive the destination buffer size, and assuming the wrong sensor length can
cause unsafe native memory access.

## Direct vendor API access

The loaded object delegates unknown attributes to the configured `ctypes.CDLL`:

```python
from ctypes import byref, c_long

burst_count = c_long(4)
status = api.SDACQMP_ParaSetBurstNumber(byref(burst_count), DEVICE_ID)
```

Direct calls use vendor-level argument and return conventions. The caller is
responsible for checking status codes and providing correctly sized pointers
and buffers.

## Hardware diagnostics

An interactive GS-1290 I/O probe is available for identifying shutter, filter,
and trigger wiring:

```powershell
python scripts/gs1290_io_probe.py --dll ".local\tec-runtime"
```

To monitor all three digital inputs while applying safe test signals:

```powershell
python scripts/gs1290_io_probe.py --dll ".local\tec-runtime" --monitor-inputs 30
```

The probe changes digital outputs. Read its warning, observe the hardware, and
confirm that connected mechanisms are safe to actuate before continuing.

## Testing

Hardware-independent tests:

```powershell
py -m unittest discover -s tests -v
```

The unit tests do not initialize connected hardware. Hardware scripts are
explicit and interactive so they cannot run accidentally as part of the normal
test suite.

## Architecture

- `tec5.sdacq` handles DLL discovery, loading, status errors, and the validated
  low-level convenience methods.
- `tec5._bindings` registers native function signatures.
- `tec5.sdacq_types` contains constants and `ctypes` structures matching the
  vendor API.
- `scripts/` contains opt-in hardware experiments and diagnostics.

A future GS-1290-specific package can depend on this library and provide device
defaults, automatic lifecycle management, calibrated spectra, and other
higher-level behavior without making the base bindings instrument-specific.

## Distribution

The repository is currently private while redistribution rights and repository
history are reviewed. See [Distribution notes](docs/distribution.md) before
publishing source, vendor binaries, documentation, or driver packages.
