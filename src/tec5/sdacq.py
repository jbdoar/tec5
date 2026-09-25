"""Thin Python access to the tec5 SDACQ64MP API.

The vendor DLL is intentionally not bundled. Call load() with its path, set
TEC5_SDACQ_DLL, or make the DLL discoverable through Windows' normal search.
"""

from __future__ import annotations

from ctypes import CDLL, byref
from dataclasses import dataclass
import os
from pathlib import Path
from typing import Any

from ._bindings import bind_functions
from .sdacq_types import CHANNEL_ID, DOUBLE, LONG, ULONG

DLL_ENV_VAR = "TEC5_SDACQ_DLL"
DLL_NAME = "SDACQ64MP.dll"


class SDACQLoadError(OSError):
    """Raised when the vendor DLL or one of its dependencies cannot be loaded."""


class SDACQError(RuntimeError):
    """Raised when an SDACQ function reports failure."""

    def __init__(self, function: str, code: int, *, value: Any = None) -> None:
        self.function = function
        self.code = code
        self.value = value
        suffix = "" if value is None else f" (returned value: {value!r})"
        super().__init__(f"{function} failed with status {code}{suffix}")


def _checked(function: str, status: int, *, value: Any = None) -> None:
    if status != 0:
        raise SDACQError(function, int(status), value=value)


def _candidate(path: os.PathLike[str] | str | None) -> Path | str:
    if path is not None:
        candidate = Path(path).expanduser()
        return candidate / DLL_NAME if candidate.is_dir() else candidate
    configured = os.environ.get(DLL_ENV_VAR)
    if configured:
        candidate = Path(configured).expanduser()
        return candidate / DLL_NAME if candidate.is_dir() else candidate
    return DLL_NAME


@dataclass(slots=True)
class SDACQLibrary:
    """A loaded and signature-configured SDACQ library.

    Unknown attributes are delegated to the underlying ctypes.CDLL. This keeps
    every bound SDACQMP_* entry point available without altering the vendor
    calling convention. The methods below cover the validated acquisition path.
    """

    _dll: CDLL
    path: Path | str
    _dll_directory: Any = None

    def __getattr__(self, name: str) -> Any:
        return getattr(self._dll, name)

    @property
    def raw(self) -> CDLL:
        """Return the configured ctypes.CDLL for direct API access."""
        return self._dll

    def init_library(self, device_type: int, flags: int = 0, res: int = 0) -> None:
        status = self.SDACQMP_InitLibrary(LONG(flags), LONG(device_type), LONG(res))
        _checked("SDACQMP_InitLibrary", status)

    def uninit_library(self, res: int = 0) -> None:
        status = self.SDACQMP_UnInitLibrary(LONG(res))
        _checked("SDACQMP_UnInitLibrary", status)

    def open_operation_electronics_device_ex(
        self,
        device_type: int,
        device_id: int,
        init_flags: int = 0,
        ip_address: int = 0,
        auth_code: int = 0,
    ) -> None:
        status = self.SDACQMP_OpenOperationElectronicsDeviceEx(
            LONG(init_flags), LONG(device_type), LONG(device_id),
            ULONG(ip_address), ULONG(auth_code),
        )
        _checked("SDACQMP_OpenOperationElectronicsDeviceEx", status)

    def initialize_operation_electronics(
        self, device_id: int, init_flags: int = 0
    ) -> None:
        status = self.SDACQMP_InitializeOperationElectronics(
            LONG(init_flags), LONG(device_id)
        )
        _checked("SDACQMP_InitializeOperationElectronics", status)

    def deinitialize_operation_electronics(self, device_id: int) -> None:
        status = self.SDACQMP_DeInitializeOperationElectronics(LONG(device_id))
        _checked("SDACQMP_DeInitializeOperationElectronics", status)

    def close_operation_electronics(self, device_id: int) -> None:
        status = self.SDACQMP_CloseOperationElectronics(LONG(device_id))
        _checked("SDACQMP_CloseOperationElectronics", status)

    def allocate_raw_data(self) -> int:
        channel_id = CHANNEL_ID()
        status = self.SDACQMP_AllocRawData(byref(channel_id))
        _checked("SDACQMP_AllocRawData", status)
        return int(channel_id.value)

    def free_raw_data(self, channel_id: int) -> None:
        value = CHANNEL_ID(channel_id)
        status = self.SDACQMP_FreeRawData(byref(value))
        _checked("SDACQMP_FreeRawData", status)

    def set_mapping(self, channel_id: int, channel: int, device_id: int) -> None:
        value = CHANNEL_ID(channel_id)
        status = self.SDACQMP_ParaSetMapping(
            byref(value), LONG(channel), LONG(device_id)
        )
        _checked("SDACQMP_ParaSetMapping", status)

    def set_integration_time(self, milliseconds: float, device_id: int) -> float:
        value = DOUBLE(milliseconds)
        status = self.SDACQMP_ParaSetIntegrationTime(byref(value), LONG(device_id))
        _checked("SDACQMP_ParaSetIntegrationTime", status, value=value.value)
        return float(value.value)

    def get_dark_current(self, device_id: int) -> None:
        status = self.SDACQMP_GetDarkCurrent(LONG(device_id))
        _checked("SDACQMP_GetDarkCurrent", status)

    def get_spectra(self, device_id: int) -> None:
        status = self.SDACQMP_GetSpectra(LONG(device_id))
        _checked("SDACQMP_GetSpectra", status)

    def set_digital_output_1(self, level: int | bool, device_id: int) -> None:
        self.set_digital_output(1, level, device_id)

    def set_digital_output(
        self, output: int, level: int | bool, device_id: int
    ) -> None:
        """Set digital output 1, 2, or 3."""
        if output not in (1, 2, 3):
            raise ValueError("output must be 1, 2, or 3")
        function_name = f"SDACQMP_IOSetDigOutput{output}"
        status = getattr(self, function_name)(LONG(int(level)), LONG(device_id))
        _checked(function_name, status)

    def get_digital_input(self, input_number: int, device_id: int) -> int:
        """Read digital input 1, 2, or 3."""
        if input_number not in (1, 2, 3):
            raise ValueError("input_number must be 1, 2, or 3")
        function_name = f"SDACQMP_IOGetDigInput{input_number}"
        level = LONG()
        status = getattr(self, function_name)(byref(level), LONG(device_id))
        _checked(function_name, status)
        return int(level.value)

    def set_sensor_work_mode(
        self, mode: int, device_id: int, flags: int = 0
    ) -> None:
        status = self.SDACQMP_ParaSetSensorWorkMode(
            LONG(flags), LONG(mode), LONG(device_id)
        )
        _checked("SDACQMP_ParaSetSensorWorkMode", status)

    def set_input_source(self, source: int, device_id: int) -> None:
        status = self.SDACQMP_ParaSetInputSource(LONG(source), LONG(device_id))
        _checked("SDACQMP_ParaSetInputSource", status)

    def set_input_latch_mode(self, mode: int, device_id: int) -> None:
        status = self.SDACQMP_ParaSetInputLatchMode(LONG(mode), LONG(device_id))
        _checked("SDACQMP_ParaSetInputLatchMode", status)

    def get_stored_raw_data(self, channel_id: int, pixel_count: int) -> list[float]:
        """Copy a scan to a buffer sized explicitly by the caller."""
        if pixel_count <= 0:
            raise ValueError("pixel_count must be positive")
        channel = CHANNEL_ID(channel_id)
        data = (DOUBLE * pixel_count)()
        status = self.SDACQMP_GetStoredRawData(byref(channel), data)
        _checked("SDACQMP_GetStoredRawData", status)
        return list(data)


def load(path: os.PathLike[str] | str | None = None) -> SDACQLibrary:
    """Load and bind the user-installed 64-bit SDACQ DLL."""
    if os.name != "nt":
        raise SDACQLoadError("tec5 SDACQ is supported only on Windows")

    candidate = _candidate(path)
    directory_handle = None
    if isinstance(candidate, Path):
        candidate = candidate.resolve()
        if not candidate.is_file():
            raise SDACQLoadError(f"SDACQ DLL not found: {candidate}")
        directory_handle = os.add_dll_directory(str(candidate.parent))
        load_target = str(candidate)
    else:
        load_target = candidate

    try:
        dll = CDLL(load_target)
        bind_functions(dll)
    except (OSError, AttributeError) as exc:
        if directory_handle is not None:
            directory_handle.close()
        raise SDACQLoadError(
            f"Could not load {load_target!r}. Install the tec5 SDACQ driver "
            f"and pass its DLL path to load(), set {DLL_ENV_VAR}, or add the "
            "vendor directory to PATH. Ensure companion DLLs are installed "
            "beside SDACQ64MP.dll."
        ) from exc

    return SDACQLibrary(dll, candidate, directory_handle)


__all__ = [
    "DLL_ENV_VAR", "DLL_NAME", "SDACQError", "SDACQLibrary",
    "SDACQLoadError", "load",
]
