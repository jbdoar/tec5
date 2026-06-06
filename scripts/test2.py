"""
Minimal GS-1290 interface.
"""

from ctypes import *
import os
import time

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# from sdacq_bindings import *

DEVICE_TYPE = 6 # PD_USB01
DEVICE_ID = 1 # that's what we set, see DIP switch on USB board
CHANNEL_ID = c_long
channel_ID = CHANNEL_ID(0)

# load DLL
dll_path = os.path.join(os.path.dirname(__file__), 'SDACQ64MP.dll')
print(dll_path)
lib = cdll.LoadLibrary(dll_path)

# Declare ctypes signatures
# InitLibrary
lib.SDACQMP_InitLibrary.argtypes = [c_long, c_long, c_long]
lib.SDACQMP_InitLibrary.restype = c_long
# OpenOperationElectronicsDeviceEx
lib.SDACQMP_OpenOperationElectronicsDeviceEx.argtypes = [c_long, c_long, c_long, c_ulong, c_ulong]
lib.SDACQMP_OpenOperationElectronicsDeviceEx.restype = c_long
# InitializeOperationElectronics
lib.SDACQMP_InitializeOperationElectronics.argtypes = [c_long, c_long]
lib.SDACQMP_InitializeOperationElectronics.restype = c_long
# AllocRawData
lib.SDACQMP_AllocRawData.argtypes = [POINTER(CHANNEL_ID)]
lib.SDACQMP_AllocRawData.restype = c_long
# ParaSetMapping
lib.SDACQMP_ParaSetMapping.argtypes = [POINTER(CHANNEL_ID), c_long, c_long]
lib.SDACQMP_ParaSetMapping.restype = c_long
# ParaSetIntegrationTime
lib.SDACQMP_ParaSetIntegrationTime.argtypes = [POINTER(c_double), c_long]
lib.SDACQMP_ParaSetIntegrationTime.restype = c_long
# GetDarkCurrent
lib.SDACQMP_GetDarkCurrent.argtypes = [c_long]
lib.SDACQMP_GetDarkCurrent.restype = c_long
# IOSetDigOutput1
lib.SDACQMP_IOSetDigOutput1.argtypes = [c_long, c_long]
lib.SDACQMP_IOSetDigOutput1.restype = c_long
# GetSpectra
lib.SDACQMP_GetSpectra.argtypes = [c_long]
lib.SDACQMP_GetSpectra.restype = c_long
# GetStoredRawData
lib.SDACQMP_GetStoredRawData.argtypes = [POINTER(CHANNEL_ID), POINTER(c_double)]
lib.SDACQMP_GetStoredRawData.restype = c_long
# FreeRawData
lib.SDACQMP_FreeRawData.argtypes = [POINTER(CHANNEL_ID)]
lib.SDACQMP_FreeRawData.restype = c_long
# DeInitializeOperationElectronics
lib.SDACQMP_DeInitializeOperationElectronics.argtypes = [c_long]
lib.SDACQMP_DeInitializeOperationElectronics.restype = c_long
# CloseOperationElectronics
lib.SDACQMP_CloseOperationElectronics.argtypes = [c_long]
lib.SDACQMP_CloseOperationElectronics.restype = c_long
# UnInitLibrary
lib.SDACQMP_UnInitLibrary.argtypes = [c_long]
lib.SDACQMP_UnInitLibrary.restype = c_long


# initialize library
lFlags = c_long(0)
l_Devicetype = c_long(DEVICE_TYPE) # def'd in sdacq32_types.h
lRes = c_long(0)
ret = lib.SDACQMP_InitLibrary(lFlags, l_Devicetype, lRes)
print("SDACQMP_InitLibrary :", ret) # 0 = OK


# open device driver and initialization

l_initflags = c_long(0)
l_ID = c_long(DEVICE_ID)
ul_IPAddress = c_ulong(0)
ul_AuthCode = c_ulong(0)
ret = lib.SDACQMP_OpenOperationElectronicsDeviceEx(l_initflags, l_Devicetype, l_ID, ul_IPAddress, ul_AuthCode)
print("SDACQMP_OpenOperationElectronicsDeviceEx: ", ret) # 0 = OK


# Initialize operation electronics
ret = lib.SDACQMP_InitializeOperationElectronics(l_initflags, l_ID)
print("SDACQMP_InitializeOperationElectronics: ", ret) # 0 = OK


# allocate memory for acquisition
ret = lib.SDACQMP_AllocRawData(byref(channel_ID))
print("SDACQMP_AllocRawData: ", ret) # 0 = OK
print("channel_ID after alloc: ", channel_ID.value)

# paraset mapping
l_channel = c_long(1) # physical channel number, 1...8
ret = lib.SDACQMP_ParaSetMapping(byref(channel_ID), l_channel, l_ID)
print("SDACQMP_ParaSetMapping: ", ret) # 0 = OK
print("channel_ID after mapping: ", channel_ID.value)


# get shutter pos
# lib.SDACQMP_IOGetDigInput1.argtypes = [POINTER(c_long), c_long]
# lib.SDACQMP_IOGetDigInput1.restype = c_long
# polarity = c_long()
# ret = lib.SDACQMP_IOGetDigInput1(byref(polarity), l_ID)
# print("SDACQMP_IOGetDigInput1: ", ret)
# print("DI1 level: ", polarity.value)



# para set integration time
INTEGRATION_TIME = 1000 # ms
integration_time = c_double(INTEGRATION_TIME) # ms
ret = lib.SDACQMP_ParaSetIntegrationTime(byref(integration_time), l_ID)
print("SDACQMP_ParaSetIntegrationTime: ", ret) # 0 = OK


# data acquisition

# dark current
ret = lib.SDACQMP_GetDarkCurrent(l_ID)
print("SDACQMP_GetDarkCurrent: ", ret) # 0 = OK


# set shutter pos
shutter_level = c_long(1)
ret = lib.SDACQMP_IOSetDigOutput1(shutter_level, l_ID)
print("SDACQMP_IOSetDigInput1: ", ret)

# shutter delay = 50ms
time.sleep(.05)

# get spectra
ret = lib.SDACQMP_GetSpectra(l_ID)
print("SDACQMP_GetSpectra: ", ret) # 0 = OK


# close shutter
shutter_level = c_long(0)
ret = lib.SDACQMP_IOSetDigOutput1(shutter_level, l_ID)
print("SDACQMP_IOSetDigInput1: ", ret)

# get stored data

MAXARRAYLENGTH = 2048
NUM_PIXELS = 1024
spectral_data = (c_double * MAXARRAYLENGTH)()
ret = lib.SDACQMP_GetStoredRawData(byref(channel_ID), spectral_data)
print("SDACQMP_GetStoredRawData: ", ret)

data = [spectral_data[i] for i in range(NUM_PIXELS)]
print(data[:10])

plt.plot(list(range(len(data))), data)
plt.savefig('test.png')
plt.show()

# free raw data
ret = lib.SDACQMP_FreeRawData(byref(channel_ID))
print("SDACQMP_FreeRawData: ", ret)

# Deinitialize operation electronics
ret = lib.SDACQMP_DeInitializeOperationElectronics(l_ID)
print("SDACQMP_DeInitializeOperationElectronics: ", ret) # 0 = OK


# Close operation electronics
ret = lib.SDACQMP_CloseOperationElectronics(l_ID)
print("SDACQMP_CloseOperationElectronics: ", ret) # 0 = OK


# Un-init library
ret = lib.SDACQMP_UnInitLibrary(lRes)
print("SDACQMP_UnInitLibrary: ", ret)



# def main():
