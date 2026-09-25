"""Python bindings for the tec5 SDACQ acquisition library."""

from .sdacq import SDACQError, SDACQLibrary, SDACQLoadError, load

__version__ = "0.2.0"

__all__ = ["SDACQError", "SDACQLibrary", "SDACQLoadError", "load"]
