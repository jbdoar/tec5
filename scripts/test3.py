"""Legacy, incomplete GS-1290 experiment."""

import argparse
from ctypes import *
import time

import matplotlib.pyplot as plt
import numpy as np

from _vendor_runtime import load_vendor_dll

# from sdacq_bindings import *






# ##########

# DEVICE_TYPE = 6 # PD_USB01
# DEVICE_ID = 1 # that's what we set, see DIP switch on USB board

# MAXARRAYLENGTH = 2048
# NUM_PIXELS = 1024

# load DLL
dll, dll_path = load_vendor_dll()
print(dll_path)
lib = dll



