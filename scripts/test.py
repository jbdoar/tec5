"""Legacy minimal GS-1290 acquisition experiment.

Init SDACQMP library, connect to device, take background-subtracted spectral scan at some integration time, plot it and save file.
"""

from ctypes import *
import time

import matplotlib.pyplot as plt

from _vendor_runtime import load_vendor_dll


# from sdacq_bindings import *


DEVICE_TYPE = 6 # PD_USB01
DEVICE_ID = 1 # that's what we set, see DIP switch on USB board

dll, dll_path = load_vendor_dll()
print(dll_path)
lib = dll


# initialize library
lib.SDACQMP_InitLibrary.argtypes = [c_long, c_long, c_long]
lib.SDACQMP_InitLibrary.restype = c_long
lFlags = c_long(0)
l_Devicetype = c_long(DEVICE_TYPE) # def'd in sdacq32_types.h
lRes = c_long(0)
ret = lib.SDACQMP_InitLibrary(lFlags, l_Devicetype, lRes)
print("SDACQMP_InitLibrary :", ret) # 0 = OK


# open device driver and initialization
lib.SDACQMP_OpenOperationElectronicsDeviceEx.argtypes = [c_long, c_long, c_long, c_ulong, c_ulong]
lib.SDACQMP_OpenOperationElectronicsDeviceEx.restype = c_long
l_initflags = c_long(0)
l_Devicetype = c_long(DEVICE_TYPE) # def'd in sdacq32_types.h
l_ID = c_long(DEVICE_ID)
ul_IPAddress = c_ulong(0)
ul_AuthCode = c_ulong(0)
ret = lib.SDACQMP_OpenOperationElectronicsDeviceEx(l_initflags, l_Devicetype, l_ID, ul_IPAddress, ul_AuthCode)
print("SDACQMP_OpenOperationElectronicsDeviceEx: ", ret) # 0 = OK


# Initialize operation electronics
lib.SDACQMP_InitializeOperationElectronics.argtypes = [c_long, c_long]
lib.SDACQMP_InitializeOperationElectronics.restype = c_long
# l_initflags = c_long(0)
# l_ID = c_long(DEVICE_ID)
ret = lib.SDACQMP_InitializeOperationElectronics(l_initflags, l_ID)
print("SDACQMP_InitializeOperationElectronics: ", ret) # 0 = OK


# allocate memory for acquisition
CHANNEL_ID = c_long
lib.SDACQMP_AllocRawData.argtypes = [POINTER(CHANNEL_ID)]
lib.SDACQMP_AllocRawData.restype = c_long
channel_ID = CHANNEL_ID(0)
ret = lib.SDACQMP_AllocRawData(byref(channel_ID))
print("SDACQMP_AllocRawData: ", ret) # 0 = OK
print("channel_ID after alloc: ", channel_ID.value)

# paraset mapping
lib.SDACQMP_ParaSetMapping.argtypes = [POINTER(CHANNEL_ID), c_long, c_long]
lib.SDACQMP_ParaSetMapping.restype = c_long
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
lib.SDACQMP_ParaSetIntegrationTime.argtypes = [POINTER(c_double), c_long]
lib.SDACQMP_ParaSetIntegrationTime.restype = c_long
integration_time = c_double(INTEGRATION_TIME) # ms
# l_ID = c_long(DEVICE_ID)
ret = lib.SDACQMP_ParaSetIntegrationTime(byref(integration_time), l_ID)
print("SDACQMP_ParaSetIntegrationTime: ", ret) # 0 = OK


# data acquisition

# dark current
lib.SDACQMP_GetDarkCurrent.argtypes = [c_long]
lib.SDACQMP_GetDarkCurrent.restype = c_long
ret = lib.SDACQMP_GetDarkCurrent(l_ID)
print("SDACQMP_GetDarkCurrent: ", ret) # 0 = OK


# set shutter pos
lib.SDACQMP_IOSetDigOutput1.argtypes = [c_long, c_long]
lib.SDACQMP_IOSetDigOutput1.restype = c_long
shutter_level = c_long(1)
ret = lib.SDACQMP_IOSetDigOutput1(shutter_level, l_ID)
print("SDACQMP_IOSetDigInput1: ", ret)

# shutter delay = 50ms
time.sleep(.05)

# get spectra
lib.SDACQMP_GetSpectra.argtypes = [c_long]
lib.SDACQMP_GetSpectra.restype = c_long
ret = lib.SDACQMP_GetSpectra(l_ID)
print("SDACQMP_GetSpectra: ", ret) # 0 = OK


# close shutter
shutter_level = c_long(0)
ret = lib.SDACQMP_IOSetDigOutput1(shutter_level, l_ID)
print("SDACQMP_IOSetDigInput1: ", ret)

# get stored data

MAXARRAYLENGTH = 2048
spectral_data = (c_double * MAXARRAYLENGTH)()
lib.SDACQMP_GetStoredRawData.argtypes = [POINTER(CHANNEL_ID), POINTER(c_double)]
lib.SDACQMP_GetStoredRawData.restype = c_long
ret = lib.SDACQMP_GetStoredRawData(byref(channel_ID), spectral_data)
print("SDACQMP_GetStoredRawData: ", ret)

data = [spectral_data[i] for i in range(1024)]
print(data[:20])

print(len(data))

plt.plot(list(range(len(data))), data)
plt.show()

# free raw data
lib.SDACQMP_FreeRawData.argtypes = [POINTER(CHANNEL_ID)]
lib.SDACQMP_FreeRawData.restype = c_long
ret = lib.SDACQMP_FreeRawData(byref(channel_ID))
print("SDACQMP_FreeRawData: ", ret)

###################################################################

# Deinitialize operation electronics
lib.SDACQMP_DeInitializeOperationElectronics.argtypes = [c_long]
lib.SDACQMP_DeInitializeOperationElectronics.restype = c_long
l_ID = c_long(DEVICE_ID)
ret = lib.SDACQMP_DeInitializeOperationElectronics(l_ID)
print("SDACQMP_DeInitializeOperationElectronics: ", ret) # 0 = OK


# Close operation electronics
lib.SDACQMP_CloseOperationElectronics.argtypes = [c_long]
lib.SDACQMP_CloseOperationElectronics.restype = c_long
l_ID = c_long(DEVICE_ID)
ret = lib.SDACQMP_CloseOperationElectronics(l_ID)
print("SDACQMP_CloseOperationElectronics: ", ret) # 0 = OK


# Un-init library
lib.SDACQMP_UnInitLibrary.argtypes = [c_long]
lib.SDACQMP_UnInitLibrary.restype = c_long
ret = lib.SDACQMP_UnInitLibrary(c_long(0))
print("SDACQMP_UnInitLibrary: ", ret)
