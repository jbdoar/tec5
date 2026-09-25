"""Resolve the locally installed tec5 runtime for legacy scripts."""

from ctypes import CDLL
import os
from pathlib import Path

DLL_NAME = "SDACQ64MP.dll"
DLL_ENV_VAR = "TEC5_SDACQ_DLL"
DEFAULT_RUNTIME_DIRECTORY = Path(__file__).resolve().parents[1] / ".local" / "tec-runtime"

# os.add_dll_directory() remains effective only while its handle is alive.
_directory_handles = []


def resolve_vendor_dll() -> Path:
    """Return the configured SDACQ DLL, defaulting to the repository runtime."""
    configured = os.environ.get(DLL_ENV_VAR)
    candidate = Path(configured).expanduser() if configured else DEFAULT_RUNTIME_DIRECTORY
    if candidate.is_dir():
        candidate /= DLL_NAME
    candidate = candidate.resolve()
    if not candidate.is_file():
        raise FileNotFoundError(
            f"SDACQ DLL not found at {candidate}. Set {DLL_ENV_VAR} to "
            "SDACQ64MP.dll or its containing directory."
        )
    return candidate


def load_vendor_dll() -> tuple[CDLL, Path]:
    """Load SDACQ64MP.dll while retaining its companion-DLL search path."""
    path = resolve_vendor_dll()
    if os.name != "nt":
        raise OSError("tec5 SDACQ is supported only on Windows")
    _directory_handles.append(os.add_dll_directory(str(path.parent)))
    return CDLL(str(path)), path
