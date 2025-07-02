from ctypes import *
import os

# from sdacq_bindings import *

# # INTERFACE
# PD_USB01 = 6
# # CONNECTOR
# DIN_FEE = 0
# # FRONTEND

# FEE_HS = 3
# # MUX
# NO_MUX = 0
# # SENSOR
# SEN_CCD_HA_S7030_4 = 7
# # SENSOR LENGTH
# PX1044 = 1044
# # MUX MODE
# NOT_AVAILABLE = 0
# # CHANNEL NUMBERS
# CHANNEL_1 = 1
# # SHUTTER_POLARITY
# SHUTTER_POL_POSITIV = 0
# SHUTTER_POL_NEGATIV = 1

# Sensor work modes
# Sensor work mode flags
# global type defs




dll_path = os.path.join(os.path.dirname(__file__), 'SDACQ64MP.dll')
lib = cdll.LoadLibrary(dll_path)

# initialize library
lib.SDACQMP_InitLibrary.argtypes = [c_long, c_long, c_long]
lib.SDACQMP_InitLibrary.restype = c_long
lFlags = c_long(0)
l_Devicetype = c_long()
lRes = c_long(0)
ret = lib.SDACQMP_InitLibrary(lFlags, l_Devicetype, lRes)
print(f"SDACQMP_InitLibrary : {ret}")

# open device driver and initialization
lib.SDACQMP_OpenOperationElectronicsDeviceEx.argtypes = [c_long, c_long, c_long, c_ulong, c_ulong]
lib.SDACQMP_OpenOperationElectronicsDeviceEx.restype = c_long
l_initflags = c_long(0)
l_Devicetype 


# allocate memory for acquisition

# change acquisition settings

# do data acquisition

# get dark current corrected data

# data processing

# finish library usage
