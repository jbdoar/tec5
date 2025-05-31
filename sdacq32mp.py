'''
Operating Electronics
for Carl Zeiss MMS/MCS Spectral Sensors
and Hamamatsu MOS Linear Image Sensors
SDACQ32MP
32/64 Bit Spectra Data Acquisition Library
PD-PCI01V1, PD-PCIe01V1, PD-USB01 and
PD-ETH01
(Windows 7/8.1/10)
'''

from ctypes import *
import os


# TODO use importlib for the path
dll_path = os.path.join(os.getcwd(), 'SDACQ64MP.dll')
_lib = cdll.LoadLibrary(dll_path)



# General functions

#SDACQMP_InitLibrary
_lib.SDACQMP_InitLibrary.argtypes = [c_long, c_long, c_long]
_lib.SDACQMP_InitLibrary.restype = c_long

#SDACQMP_UnInitLibrary
_lib.SDACQMP_UnInitLibrary.argtypes = c_long
_lib.SDACQMP_UnInitLibrary.restype = c_long

#SDACQMP_OpenOperationElectronicsDeviceEx
_lib.SDACQMP_OpenOperationElectronicsDeviceEx.argtypes = [c_long, c_long, c_long, c_ulong, c_ulong]
_lib.SDACQMP_OpenOperationElectronicsDeviceEx.restype = c_long

#SDACQMP_InitializeOperationElectronics
_lib.SDACQMP_InitializeOperationElectronics.argtypes = [c_long, c_long]
_lib.SDACQMP_InitializeOperationElectronics.restype = c_long

#SDACQMP_DeInitializeOperationElectronics
_lib.SDACQMP_DeInitializeOperationElectronics.argtypes = c_long
_lib.SDACQMP_DeInitializeOperationElectronics.restype = c_long

#SDACQMP_CloseOperationElectronics
_lib.SDACQMP_CloseOperationElectronics.argtypes = c_long
_lib.SDACQMP_CloseOperationElectronics.restype = c_long

#SDACQMP_ParaSetSensorWorkMode
_lib.SDACQMP_ParaSetSensorWorkMode.argtypes = [c_long, c_long, c_long]
_lib.SDACQMP_ParaSetSensorWorkMode.restype = c_long

#SDACQMP_ParaSetIntegrationTime
_lib.SDACQMP_ParaSetIntegrationTime.argtypes = [POINTER(c_double), c_long]
_lib.SDACQMP_ParaSetIntegrationTime.restype = c_long

#SDACQMP_ParaSetIntegrationTime2
_lib.SDACQMP_ParaSetIntegrationTime2.argtypes = [POINTER(c_long), c_long]
_lib.SDACQMP_ParaSetIntegrationTime2.restype = c_long

#SDACQMP_ParaSetIntegrationTime3
_lib.SDACQMP_ParaSetIntegrationTime3.argtypes = [POINTER(c_long), c_long]
_lib.SDACQMP_ParaSetIntegrationTime3.restype = c_long

#SDACQMP_ParaSetIntegrationTimeForDeleting
_lib.SDACQMP_ParaSetIntegrationTimeForDeleting.argtypes = [POINTER(c_double), c_long]
_lib.SDACQMP_ParaSetIntegrationTimeForDeleting.restype = c_long

#SDACQMP_ParaSetAverageNumber
_lib.SDACQMP_ParaSetAverageNumber.argtypes = [POINTER(c_long), c_long]
_lib.SDACQMP_ParaSetAverageNumber.restype = c_long

#SDACQMP_ParaGetAverageNumberLimit
_lib.SDACQMP_ParaGetAverageNumberLimit.argtypes = [POINTER(c_long), c_long]
_lib.SDACQMP_ParaGetAverageNumberLimit.restype = c_long

#SDACQMP_ParaSetBurstNumber
_lib.SDACQMP_ParaSetBurstNumber.argtypes = [POINTER(c_long), c_long]
_lib.SDACQMP_ParaSetBurstNumber.restype = c_long

#SDACQMP_ParaGetBurstNumberLimit
_lib.SDACQMP_ParaGetBurstNumberLimit.argtypes = [POINTER(c_long), c_long]
_lib.SDACQMP_ParaGetBurstNumberLimit.restype = c_long

#SDACQMP_ParaSetHardwareFlashMode2
_lib.SDACQMP_ParaSetHardwareFlashMode2.argtypes = [c_long, c_long, c_long]
_lib.SDACQMP_ParaSetHardwareFlashMode2.restype = c_long

#SDACQMP_ParaSetFlashPolarity
_lib.SDACQMP_ParaSetFlashPolarity.argtypes = [c_long, c_long]
_lib.SDACQMP_ParaSetFlashPolarity.restype = c_long

#SDACQMP_ParaGetHardwareFlashMode
_lib.SDACQMP_ParaGetHardwareFlashMode.argtypes = [POINTER(c_long), c_long]
_lib.SDACQMP_ParaGetHardwareFlashMode.restype = c_long

#SDACQMP_ParaSetExtTriggTimeout
_lib.SDACQMP_ParaSetExtTriggTimeout.argtypes = [POINTER(c_long), c_long]
_lib.SDACQMP_ParaSetExtTriggTimeout.restype = c_long

#SDACQMP_ParaSetDarkCurrentCorrectionMode
_lib.SDACQMP_ParaSetDarkCurrentCorrectionMode.argtypes = [POINTER(CHANNEL_ID), c_long]
_lib.SDACQMP_ParaSetDarkCurrentCorrectionMode.restype = c_long

#SDACQMP_ParaSetShutterPolarity
_lib.SDACQMP_ParaSetShutterPolarity.argtypes = [c_long, c_long]
_lib.SDACQMP_ParaSetShutterPolarity.restype = c_long

#SDACQMP_ParaSetShutterControlMode
_lib.SDACQMP_ParaSetShutterControlMode.argtypes = [c_long, c_long]
_lib.SDACQMP_ParaSetShutterControlMode.restype = c_long

#SDACQMP_ParaGetIntegrationTimeLimits
_lib.SDACQMP_ParaGetIntegrationTimeLimits.argtypes = [POINTER(c_double), POINTER(c_double), c_long]
_lib.SDACQMP_ParaGetIntegrationTimeLimits.restype = c_long

#SDACQMP_ParaGetIntensityLimits
_lib.SDACQMP_ParaGetIntensityLimits.argtypes = [POINTER(c_long), POINTER(c_long), c_long]
_lib.SDACQMP_ParaGetIntensityLimits.restype = c_long

#SDACQMP_ParaSetSpecBuffer
_lib.SDACQMP_ParaSetSpecBuffer.argtypes = [c_long, c_long]
_lib.SDACQMP_ParaSetSpecBuffer.restype = c_long

#SDACQMP_ParaSetROISettings
_lib.SDACQMP_ParaSetROISettings.argtypes = [c_long, POINTER(P_ROI_PARAMETERSET), c_long, c_long]
_lib.SDACQMP_ParaSetROISettings.restype = c_long

#SDACQMP_GetSpectra
_lib.SDACQMP_GetSpectra.argtypes = c_long
_lib.SDACQMP_GetSpectra.restype = c_long

#SDACQMP_GetSpectraEx
_lib.SDACQMP_GetSpectraEx.argtypes = [c_long, c_long]
_lib.SDACQMP_GetSpectraEx.restype = c_long

#SDACQMP_GetDarkCurrent
_lib.SDACQMP_GetDarkCurrent.argtypes = c_long
_lib.SDACQMP_GetDarkCurrent.restype = c_long

#SDACQMP_GetDarkCurrentWithShutter
_lib.SDACQMP_GetDarkCurrentWithShutter.argtypes = [c_long, c_long]
_lib.SDACQMP_GetDarkCurrentWithShutter.restype = c_long

#SDACQMP_GetBufferedSpectra
_lib.SDACQMP_GetBufferedSpectra.argtypes = [POINTER(c_long), POINTER(c_long), c_long]
_lib.SDACQMP_GetBufferedSpectra.restype = c_long

#SDACQMP_SetInterfaceActive
_lib.SDACQMP_SetInterfaceActive.argtypes = c_long
_lib.SDACQMP_SetInterfaceActive.restype = c_long

#SDACQMP_SetInterfaceInActive
_lib.SDACQMP_SetInterfaceInActive.argtypes = c_long
_lib.SDACQMP_SetInterfaceInActive.restype = c_long

#SDACQMP_IOSetDigOutput1
_lib.SDACQMP_IOSetDigOutput1.argtypes = [c_long, c_long]
_lib.SDACQMP_IOSetDigOutput1.restype = c_long

#SDACQMP_IOSetDigOutput2
_lib.SDACQMP_IOSetDigOutput2.argtypes = [c_long, c_long]
_lib.SDACQMP_IOSetDigOutput2.restype = c_long

#SDACQMP_IOSetDigOutput3
_lib.SDACQMP_IOSetDigOutput3.argtypes = [c_long, c_long]
_lib.SDACQMP_IOSetDigOutput3.restype = c_long

#SDACQMP_IOSetDigOutputs
_lib.SDACQMP_IOSetDigOutputs.argtypes = [c_long, c_long, c_long]
_lib.SDACQMP_IOSetDigOutputs.restype = c_long

#SDACQMP_IOGetDigInput1
_lib.SDACQMP_IOGetDigInput1.argtypes = [POINTER(c_long), c_long]
_lib.SDACQMP_IOGetDigInput1.restype = c_long

#SDACQMP_IOGetDigInput2
_lib.SDACQMP_IOGetDigInput2.argtypes = [POINTER(c_long), c_long]
_lib.SDACQMP_IOGetDigInput2.restype = c_long

#SDACQMP_IOGetDigInput3
_lib.SDACQMP_IOGetDigInput3.argtypes = [POINTER(c_long), c_long]
_lib.SDACQMP_IOGetDigInput3.restype = c_long

#SDACQMP_IOGetDigInputs
_lib.SDACQMP_IOGetDigInputs.argtypes = [POINTER(c_long), c_long, c_long]
_lib.SDACQMP_IOGetDigInputs.restype = c_long

#SDACQMP_ParaSetInputSource
_lib.SDACQMP_ParaSetInputSource.argtypes = [c_long, c_long]
_lib.SDACQMP_ParaSetInputSource.restype = c_long

#SDACQMP_ParaSetInputLatchMode
_lib.SDACQMP_ParaSetInputLatchMode.argtypes = [c_long, c_long]
_lib.SDACQMP_ParaSetInputLatchMode.restype = c_long

#SDACQMP_GetErrorCode
_lib.SDACQMP_GetErrorCode.argtypes = [POINTER(P_LLERRORS)]
_lib.SDACQMP_GetErrorCode.restype = c_long

#SDACQMP_WarningMessagesEx
_lib.SDACQMP_WarningMessagesEx.argtypes = [c_long, c_long]
_lib.SDACQMP_WarningMessagesEx.restype = c_long

#SDACQMP_ParaSetMUXMode
_lib.SDACQMP_ParaSetMUXMode.argtypes = [c_long, c_long, c_long]
_lib.SDACQMP_ParaSetMUXMode.restype = c_long

#SDACQMP_ParaSetMUXActiveChannel
_lib.SDACQMP_ParaSetMUXActiveChannel.argtypes = [c_long, c_long]
_lib.SDACQMP_ParaSetMUXActiveChannel.restype = c_long

#SDACQMP_AllocRawData
_lib.SDACQMP_AllocRawData.argtypes = POINTER(CHANNEL_ID)
_lib.SDACQMP_AllocRawData.restype = c_long

#SDACQMP_ParaSetMapping
_lib.SDACQMP_ParaSetMapping.argtypes = [POINTER(CHANNEL_ID), c_long, c_long]
_lib.SDACQMP_ParaSetMapping.restype = c_long

#SDACQMP_FreeRawData
_lib.SDACQMP_FreeRawData.argtypes = POINTER(CHANNEL_ID)
_lib.SDACQMP_FreeRawData.restype = c_long

#SDACQMP_LS_Initialize
_lib.SDACQMP_LS_Initialize.argtypes = [c_long, c_long, c_long, POINTER(c_long)]
_lib.SDACQMP_LS_Initialize.restype = c_long

#SDACQMP_LS_OpenShutter
_lib.SDACQMP_LS_OpenShutter.argtypes = [c_long, c_long, c_long]
_lib.SDACQMP_LS_OpenShutter.restype = c_long

#SDACQMP_LS_CloseShutter
_lib.SDACQMP_LS_CloseShutter.argtypes = [c_long, c_long, c_long]
_lib.SDACQMP_LS_CloseShutter.restype = c_long

#SDACQMP_LS_PowerON
_lib.SDACQMP_LS_PowerON.argtypes = [c_long, c_long, c_long, c_long]
_lib.SDACQMP_LS_PowerON.restype = c_long

#SDACQMP_LS_PowerOFF
_lib.SDACQMP_LS_PowerOFF.argtypes = [c_long, c_long, c_long, c_long]
_lib.SDACQMP_LS_PowerOFF.restype = c_long

#SDACQMP_LS_GetShutterPosition
_lib.SDACQMP_LS_GetShutterPosition.argtypes = [c_long, c_long, POINTER(c_long)]
_lib.SDACQMP_LS_GetShutterPosition.restype = c_long

#SDACQMP_LS_GetStatus
_lib.SDACQMP_LS_GetStatus.argtypes = [c_long, c_long, POINTER(c_long)]
_lib.SDACQMP_LS_GetStatus.restype = c_long

#SDACQMP_LS_GetActualTemperature
_lib.SDACQMP_LS_GetActualTemperature.argtypes = [c_long, c_long, POINTER(c_long)]
_lib.SDACQMP_LS_GetActualTemperature.restype = c_long

#SDACQMP_LS_SetTemperatureAlarm
_lib.SDACQMP_LS_SetTemperatureAlarm.argtypes = [c_long, c_long, c_long, c_long]
_lib.SDACQMP_LS_SetTemperatureAlarm.restype = c_long

#SDACQMP_LS_ReadFlashRate
_lib.SDACQMP_LS_ReadFlashRate.argtypes = [c_long, c_long, POINTER(c_long)]
_lib.SDACQMP_LS_ReadFlashRate.restype = c_long

#SDACQMP_LS_SetFlashCounter
_lib.SDACQMP_LS_SetFlashCounter.argtypes = [c_long, c_long, c_long]
_lib.SDACQMP_LS_SetFlashCounter.restype = c_long

#SDACQMP_LS_GetRemoteStatus
_lib.SDACQMP_LS_GetRemoteStatus.argtypes = [c_long, c_long, POINTER(c_long)]
_lib.SDACQMP_LS_GetRemoteStatus.restype = c_long

#SDACQMP_LS_SavePowerStatus
_lib.SDACQMP_LS_SavePowerStatus.argtypes = [c_long, c_long]
_lib.SDACQMP_LS_SavePowerStatus.restype = c_long

#SDACQMP_LS_GetSTRProperty
_lib.SDACQMP_LS_GetSTRProperty.argtypes = [c_long, c_long, LS_Property, c_long, POINTER(c_char)]
_lib.SDACQMP_LS_GetSTRProperty.restype = c_long

#SDACQMP_LS_GetLNGProperty
_lib.SDACQMP_LS_GetLNGProperty.argtypes = [c_long, c_long, LS_Property, POINTER(c_long)]
_lib.SDACQMP_LS_GetLNGProperty.restype = c_long

#SDACQMP_LS_SetLNGProperty
_lib.SDACQMP_LS_SetLNGProperty.argtypes = [c_long, c_long, LS_Property, c_long]
_lib.SDACQMP_LS_SetLNGProperty.restype = c_long

#SDACQMP_LS_GetDBLProperty
_lib.SDACQMP_LS_GetDBLProperty.argtypes = [c_long, c_long, LS_Property, POINTER(c_double)]
_lib.SDACQMP_LS_GetDBLProperty.restype = c_long

#SDACQMP_LS_SetDBLProperty
_lib.SDACQMP_LS_SetDBLProperty.argtypes = [c_long, c_long, LS_Property, c_double]
_lib.SDACQMP_LS_SetDBLProperty.restype = c_long

#SDACQMP_HWConfig_ChangeLSParams
_lib.SDACQMP_HWConfig_ChangeLSParams.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long]
_lib.SDACQMP_HWConfig_ChangeLSParams.restype = c_long

#SDACQMP_HWConfig_GetLSParams
_lib.SDACQMP_HWConfig_GetLSParams.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long]
_lib.SDACQMP_HWConfig_GetLSParams.restype = c_long

#SDACQMP_GetStoredRawData
_lib.SDACQMP_GetStoredRawData.argtypes = [CHANNEL_ID, POINTER(c_double)]
_lib.SDACQMP_GetStoredRawData.restype = c_long

#SDACQMP_GetStoredRawDataBurst
_lib.SDACQMP_GetStoredRawDataBurst.argtypes = [CHANNEL_ID, c_long, POINTER(c_double)]
_lib.SDACQMP_GetStoredRawDataBurst.restype = c_long

#SDACQMP_GetStoredPixelnumber
_lib.SDACQMP_GetStoredPixelnumber.argtypes = [POINTER(CHANNEL_ID), POINTER(c_double)]
_lib.SDACQMP_GetStoredPixelnumber.restype = c_long

#SDACQMP_GetStoredDarkcurrentData
_lib.SDACQMP_GetStoredDarkcurrentData.argtypes = [POINTER(CHANNEL_ID), POINTER(c_double)]
_lib.SDACQMP_GetStoredDarkcurrentData.restype = c_long

#SDACQMP_DeleteDarkcurrentData
_lib.SDACQMP_DeleteDarkcurrentData.argtypes = POINTER(CHANNEL_ID)
_lib.SDACQMP_DeleteDarkcurrentData.restype = c_long

#SDACQMP_GetStoredDarkModeSettings
_lib.SDACQMP_GetStoredDarkModeSettings.argtypes = [POINTER(CHANNEL_ID), POINTER(c_long)]
_lib.SDACQMP_GetStoredDarkModeSettings.restype = c_long

#SDACQMP_GetStoredAverageNumber
_lib.SDACQMP_GetStoredAverageNumber.argtypes = [POINTER(CHANNEL_ID), POINTER(c_long)]
_lib.SDACQMP_GetStoredAverageNumber.restype = c_long

#SDACQMP_GetStoredBurstNumber
_lib.SDACQMP_GetStoredBurstNumber.argtypes = [POINTER(CHANNEL_ID), POINTER(c_long)]
_lib.SDACQMP_GetStoredBurstNumber.restype = c_long

#SDACQMP_GetStoredIntegrationtime
_lib.SDACQMP_GetStoredIntegrationtime.argtypes = [POINTER(CHANNEL_ID), POINTER(c_double)]
_lib.SDACQMP_GetStoredIntegrationtime.restype = c_long

#SDACQMP_GetStoredTimeStamp
_lib.SDACQMP_GetStoredTimeStamp.argtypes = [POINTER(CHANNEL_ID), c_long, POINTER(c_long), POINTER(_TIMEDATE_EXT), POINTER(c_longlong)]
_lib.SDACQMP_GetStoredTimeStamp.restype = c_long

#SDACQMP_GetStoredIntensity
_lib.SDACQMP_GetStoredIntensity.argtypes = [POINTER(CHANNEL_ID), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)] 
_lib.SDACQMP_GetStoredIntensity.restype = c_long

#SDACQMP_HWConfig_GetSensorParamsEx2
_lib.SDACQMP_HWConfig_GetSensorParamsEx2.argtypes = [c_long, POINTER(_SENSORPARAMS_X), c_long, c_long]
_lib.SDACQMP_HWConfig_GetSensorParamsEx2.restype = c_long

#SDACQMP_HWConfig_ChangeSensorParamsEx2
_lib.SDACQMP_HWConfig_ChangeSensorParamsEx2.argtypes = [c_long, POINTER(_SENSORPARAMS_X), c_long, c_long]
_lib.SDACQMP_HWConfig_ChangeSensorParamsEx2.restype = c_long

#SDACQMP_HWConfig_ParaGetHWConfigurationEx2
_lib.SDACQMP_HWConfig_ParaGetHWConfigurationEx2.argtypes = [c_long, POINTER(_HWSETTINGS_X), c_long]
_lib.SDACQMP_HWConfig_ParaGetHWConfigurationEx2.restype = c_long

#SDACQMP_HWConfig_ChangeMUXParams
_lib.SDACQMP_HWConfig_ChangeMUXParams.argtypes = [c_long, c_long, c_long, c_long]
_lib.SDACQMP_HWConfig_ChangeMUXParams.restype = c_long

#SDACQMP_HWConfig_GetMUXParams
_lib.SDACQMP_HWConfig_GetMUXParams.argtypes = [POINTER(c_long), POINTER(c_long), POINTER(c_long), POINTER(c_long)]
_lib.SDACQMP_HWConfig_GetMUXParams.restype = c_long

#SDACQMP_I2C_Write_1
_lib.SDACQMP_I2C_Write_1.argtypes = [c_long, POINTER(c_ubyte), c_long, c_long]
_lib.SDACQMP_I2C_Write_1.restype = c_long

#SDACQMP_I2C_Read_1
_lib.SDACQMP_I2C_Read_1.argtypes = [c_long, POINTER(c_ubyte), c_long, c_long]
_lib.SDACQMP_I2C_Read_1.restype = c_long

#SDACQMP_I2C_Write_N
_lib.SDACQMP_I2C_Write_N.argtypes = [c_long, POINTER(c_ubyte), c_long, c_long, c_long]
_lib.SDACQMP_I2C_Write_N.restype = c_long

#SDACQMP_I2C_Read_N
_lib.SDACQMP_I2C_Read_N.argtypes =
_lib.SDACQMP_I2C_Read_N.restype = c_long

#SDACQMP_I2C_Programming
_lib.SDACQMP_I2C_Programming.argtypes =
_lib.SDACQMP_I2C_Programming.restype = c_long

#SDACQMP_I2C_Read_EEPROM_CustData
_lib.SDACQMP_I2C_Read_EEPROM_CustData.argtypes =
_lib.SDACQMP_I2C_Read_EEPROM_CustData.restype = c_long

#SDACQMP_I2C_Write_EEPROM_CustData
_lib.SDACQMP_I2C_Write_EEPROM_CustData.argtypes =
_lib.SDACQMP_I2C_Write_EEPROM_CustData.restype = c_long

#SDACQMP_I2C_Read_EEPROM
_lib.SDACQMP_I2C_Read_EEPROM.argtypes =
_lib.SDACQMP_I2C_Read_EEPROM.restype = c_long

#SDACQMP_I2C_Write_EEPROM
_lib.SDACQMP_I2C_Write_EEPROM.argtypes =
_lib.SDACQMP_I2C_Write_EEPROM.restype = c_long

#SDACQMP_I2C_GetAllTemperatures
_lib.SDACQMP_I2C_GetAllTemperatures.argtypes =
_lib.SDACQMP_I2C_GetAllTemperatures.restype = c_long

#SDACQMP_I2C_GetTemperature
_lib.SDACQMP_I2C_GetTemperature.argtypes =
_lib.SDACQMP_I2C_GetTemperature.restype = c_long

#SDACQMP_Linearization
_lib.SDACQMP_Linearization.argtypes =
_lib.SDACQMP_Linearization.restype = c_long

#SDACQMP_LinearizationChannel
_lib.SDACQMP_LinearizationChannel.argtypes =
_lib.SDACQMP_LinearizationChannel.restype = c_long

#SDACQMP_LinearizationChannelEx
_lib.SDACQMP_LinearizationChannelEx.argtypes =
_lib.SDACQMP_LinearizationChannelEx.restype = c_long


def SDACQMP_InitLibrary() -> int:
    """
    Parameters:
    LONG lFlags (0)
    LONG l_Devicetype (defined in sdacq32_types.h)
    LONG lRes (0)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Initialization of the SDACQ32MP library
    This function has to be called once before calling any other SDACQMP function in any application.
    """
    pass

def SDACQMP_UnInitLibrary() -> int:
    """
    Parameters:
    LONG lRes (0)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Deintialization of the SDACQMP library.
    This function has to be called once after closing the last opened operating electronics as last SDACQMP function call in any application.
    """
    pass

def SDACQMP_OpenOperationElectronicsDeviceEx() -> int:
    """
    Parameters:
    LONG l_initflags
        Bit 0 = 1: suppresses errors during initialization
        Bit 1 = 1: don’t close interface if function fails, because of non-initialized data in EEPROMs, should be 0 otherwise
        Bit 3 = 1: suppress automatic configuration
        Other bits are reserved and must be 0.
    LONG l_Devicetype (defined in sdacq32_types.h)
    LONG l_ID (1..MAXINTERFACE)
    ULONG ul_IPAddress (PD_ETH01 only, 0 otherwise)
    ULONG ul_AuthCode (Default = 0 = no authorization code)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function allocates memory for a specified interface,
    opens the kernel mode device respectively initiates a connection
    to the device and links it as interface number ‘l_ID’.

    Remarks:
    PD-ETH01: IP-address and device ID configuration must
    be done in advance via its web interface.
    other: set ul_IPAddress and ul_AuthCode to 0 (not used).
    """
    pass

def SDACQMP_InitializeOperationElectronics() -> int:
    """
    Parameters:
    LONG l_initflags (Bit 0 = 1: suppresses errors during initialization)
    LONG l_ID (1..MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Initialization of the interface card with automatic configuration (PnP)
    These values will be reset to the related default values:
    Integration time for acquisition: 2x minimum integration time
    Integration time for deleting: 2x minimum integration time
    Average number: 1 (after first initialization)
    Hardware flash: inactive
    Ext. triggering timeout time: 60 seconds
    Shutter polarity: positive
    Reset all DOUTs
    """
    pass

def SDACQMP_DeInitializeOperationElectronics() -> int:
    """
    Parameters:
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Deinitialization of the interface, no access is possible before new initialization.
    """
    pass

def SDACQMP_CloseOperationElectronics() -> int:
    """
    Parameters:
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function closes the handle of the kernel mode device and deallocates its memory, no access is possible before reopen the device.
    """
    pass

# Parameter functions

def SDACQMP_ParaSetSensorWorkMode() -> int:
    """
    Parameters:
    LONG l_workflags
    Bit 0 = 1: suppresses errors during initialization
    Bit 1 = 1: suppresses FIFO overflow protection
    Bit 2 = 1: enable external trigger ready signal (DOUT3)
    Bit 4 = 1: enable external trigger rising edge
    LONG l_sensorworkmode (defined in sdacq32_types.h)
    StartNewScanWithCleaning
    StartNewScanWithoutCleaning
    SyncToContScan
    ExternalTriggerSlope
    ExternalTriggerPulse
    GetLastScan
    GetBufferedScan
    ExternalTriggerSlopeWithCleaning
    ExternalTriggerPulseWithCleaning
    […]
    LONG l_ID (1...MAXINTERFACE)

    Return Value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Initialization of the chosen interface in the new sensor work mode with current values.

    For more information about the sensor work modes a document
    ‘Overview Sensor Operating Modes’ is available on our CD.

    Attention (USB electronics and PD-ETH01):
    GetLastScan / GetBufferedScan / other buffered modes:
    These buffered modes do not allow to do read / write I²C operations simultaneously. In such
    cases the function stops the current sensor work mode before execution of the I²C operation,
    starts the sensor work mode ‘SyncToContScan’ instead, executes the I²C operation and restarts the previously set sensor work mode again.
    Note that buffered spectral data get lost after such procedure e.g. switching the shutter.
    I²C operations are used as built-in operations in
    several sdacq32mp functions:
    - SDACQMP_GetDarkCurrentWithShutter()
    - SDACQMP_ParaSetShutterControlMode()
    - SDACQMP_ParaSetShutterPolarity()
    - SDACQMP_LS_xxx functions()
    - SDACQMP_I2C_xxx functions()
    - SDACQMP_HWConfig_xxx functions()
    - SDACQMP_GetActualConfigurationEx()
    """
    pass

def SDACQMP_ParaSetIntegrationTime() -> int:
    """
    Parameters:
    PDOUBLE pd_inttime (pointer to a double value [unit: ms])
    LONG l_ID (1...MAXINTERFACE)
    
    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function sets new integration time in [ms] for the spectral data acquisition of the selected interface and you will get back the new limited integration time depending on the current settings, returns ‘NOK’ if value is limited.
    This function should be used generally.
    """
    pass

def SDACQMP_ParaSetIntegrationTime2() -> int:
    """
    Parameters:
    PLONG pl_inttime (pointer to a long value [unit: ms])
    LONG l_ID (1...MAXINTERFACE)
    
    Return value:
    LONG (0 = OK, -1 = NOK = error level)
    
    Description:
    Function sets new integration time in [ms] for the spectral data acquisition of the selected interface and you will get back the new limited integration time depending on the current settings, returns ‘NOK’ if value is limited.
    The difference to SDACQMP_ParaSetIntegrationTime() is the timer resolution which is 1 ms instead of 0.1 ms (Standard) so it is possible to use a larger integration time up to 65 seconds.

    Remarks:
    Not available for PD-ETH01:
    The function SDACQMP_ParaSetIntegrationTime() operates with a resolution of 1 us with an enhanced range and can be used instead.
    """
    pass

def SDACQMP_ParaSetIntegrationTime3() -> int:
    """
    Parameters: PLONG pl_inttime (pointer to a long value [unit: ms])
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function sets new integration time in [ms] for the spectral data acquisition of the selected interface and you will get back the new limited integration time depending on the current settings, returns ‘NOK’ if value is limited.
    The difference to SDACQMP_ParaSetIntegrationTime() is the timer resolution which is 8 ms instead of 0.1 ms (Standard) so it is possible to use a larger integration time up to 520 seconds.
    This function is supported for PD-PCI01V1 and PD-USB01 (since CPLD version 2.04 and driver version 2.0.1.3) only.

    Remarks:
    Not available for PD-ETH01:
    The function SDACQMP_ParaSetIntegrationTime() operates with a resolution of 1 us with an enhanced range and can be used instead.
    """
    pass

def SDACQMP_ParaSetIntegrationTimeForDeleting() -> int:
    """
    Parameters:
    PDOUBLE pd_inttime (pointer to a double value [unit: ms])
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function sets new integration time in [ms] for sensor continuous
    readout (cleaning scans) in sensor modes which employ cleaning
    scans with a configurable integration time of the selected interface
    and you will receive the new limited integration time depending on the
    current settings, returns ‘NOK’ if value is limited or function fails.
    """
    pass

def SDACQMP_ParaSetAverageNumber() -> int:
    """
    Parameters:
    PLONG pl_average (pointer to a long value)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function sets new average number (1 … 100) for the spectral data
    acquisition of the selected interface and changes acquisition from
    “burst” to “averaging” mode.
    You will receive the new limited average number time depending on
    the current settings, returns ‘NOK’ if value is limited.
    """
    pass

def SDACQMP_ParaGetAverageNumberLimit() -> int:
    """
    Parameters:
    PLONG pl_MaxAverage (pointer to a long value)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function gets maximum average number (1 … 255) for the spectral
    data acquisition of the selected interface.
    """
    pass

def SDACQMP_ParaSetBurstNumber() -> int:
    """
    Parameters:
    PLONG pl_burst (pointer to a long value)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function sets new burst number for the spectral data acquisition of the
    selected interface and changes acquisition from “averaging” to “burst”
    mode. After calling this function every use of
    “SDACQMP_GetSpectra” starts a burst acquisition of “l_burst” spectra. To change the acquistion mode to standard averaging use the
    function SDACQMP_ParaSetAverageNumber, returns ‘NOK’ if value
    is limited.
    """
    pass

def SDACQMP_ParaGetBurstNumberLimit() -> int:
    """
    Parameters:
    PLONG pl_MaxBurst (pointer to a long value)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function gets maximum burst number for the spectral data acquisition
    of the selected interface.
    """
    pass

def SDACQMP_ParaSetHardwareFlashMode2() -> int:
    """
    Parameters:
    LONG l_active (TRUE / FALSE)
    LONG l_mode (TRUE / FALSE)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function enables or disables hardware flash during the spectral data
    acquisition. Set l_mode to 0 (FALSE) to enable the flash signal together with the EOS (End of Scan) signal of the data scan (Default) or
    set it to TRUE to enable the signal together with the ST_SCAN (Start
    of Scan) signal of the data scan of the selected interface. Note that
    not all interface electronics do support flash triggering together with
    the ST_SCAN signal. In such cases a specific error occures.
    """
    pass

def SDACQMP_ParaSetFlashPolarity() -> int:
    """
    Parameters:
    LONG l_flashpolarity (1 := Positive)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function sets the polarity of the flash output signal. The signal has
    negative polarity by default. This can be changed by setting
    l_flashpolarity to 1.
    """
    pass

def SDACQMP_ParaGetHardwareFlashMode() -> int:
    """
    Parameters:
    PLONG pl_active (TRUE / FALSE)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function gets the actual status of the hardware flash of the selected
    interface. If hardware flash mode is enabled ‘pl_active’ is TRUE otherwise ‘FALSE’.
    """
    pass

def SDACQMP_ParaSetExtTriggTimeout() -> int:
    """
    Parameters:
    PLONG pl_timeouttime (pointer to a long value)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function sets the timeout time [ms] for externally triggered sensor operating modes, returns ‘NOK’ if value is limited.
    """
    pass

def SDACQMP_ParaSetDarkCurrentCorrectionMode() -> int:
    """
    Parameters:
    CHANNEL_ID *channel_ID
    LONG l_darkcorr (true enable, false disable)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function enables / disables the automatic dark current correction for
    the specified channel. Dark current correction is enabled by default for
    all channels.
    """
    pass

def SDACQMP_ParaSetShutterPolarity() -> int:
    """
    Parameters:
    LONG l_shutterpolarity (true for negative, false for positive)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function sets shutter polarity, specifies the digital output level to close
    the shutter, Standard setting is ‘false’ to close the shutter by setting
    digital output #2 to ‘high’ = +5 V.
    In case of negative polarity the digital output #2 is set to ‘low’ = 0 V for
    closing the shutter.
    """
    pass

def SDACQMP_ParaSetShutterControlMode() -> int:
    """
    Parameters:
    LONG l_shutter_ctrl_mode
    - SCM_DEFAULT_OPEN (Default)
    - SCM_DEFAULT_CLOSED
    - SCM_DEFAULT_OPEN_V1 (legacy mode)
    LONG l_delaytime (delay time in ms)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function sets the shutter control mode. If shutter control mode is
    SCM_DEFAULT_OPEN (default) the shutter is only closed during the
    dark current data acquisition. To open the shutter only during spectral
    data acquisition use SCM_DEFAULT_CLOSED as parameter.
    The delay time is to make sure the shutter has enough time to completely close or open. (see description of the function
    SDACQMP_GetDarkCurrentWithShutter).
    Use legacy mode SCM_DEFAULT_OPEN_V1 for compatibility with
    SCM_DEFAULT_OPEN of version 1.x of the SDACQ32MP library if
    there are problems with shutter control after updating an existing application to version 2.x.
    Note: If shutter control mode is SCM_DEFAULT_CLOSED the processing of function
    SDACQMP_GetSpectra is similar to SDACQMP_GetDarkCurrentWithShutter.
    The value ‘l_delaytime’ can be 0, if a LS component with automatic shutter control is
    used.
    """
    pass

def SDACQMP_ParaGetIntegrationTimeLimits() -> int:
    """
    Parameters:
    PDOUBLE pd_low
    PDOUBLE pd_high
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function gets the actual integration time limits in [ms]
    This function should be called only after the hardware is configured
    and initialized. If large integration time values are used (enabled before with one of the functions SDACQMP_ParaSetIntegrationTime2()
    or SDACQMP_ParaSetIntegrationTime3()) this function retrieves the
    limits of the larger range with a lower resolution.
    """
    pass

def SDACQMP_ParaGetIntensityLimits() -> int:
    """
    Parameters:
    PLONG pl_low
    PLONG pl_high
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function gets the actual min. and max. intensity counts
    """
    pass

def SDACQMP_ParaSetSpecBuffer() -> int:
    """
    Parameters:
    LONG l_SpecBufferSize (1…256)
    Number of buffered spectra
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    The function is only applicable to asynchronous buffered sensor work
    modes (i.e. GetBufferedScan).
    Call this function to specify how many spectra are to be buffered. The
    default in sensor work mode GetBufferedScan is 12.
    """
    pass

def SDACQMP_ParaSetROISettings() -> int:
    """
    Parameters:
    LONG l_Reserved (must be 0, for later use)
    P_ROI_PARAMETERSET pROIData (ROI information)
    LONG l_channel (must be 0, for later use)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (>=0 = OK, <0 = NOK)

    Description:
    This function sets Region Of Interest information, which reduces the
    transferred scan data amount to the pixel range required by the application.

    Remarks:
    PD-ETH01 /DP only

    typedef struct _P_ROI_PARAMETERSET
    {
    long lSize; // size of struct [number of bytes]
    long lVersion; // must be 0
    unsigned short usROI[2][2]; // 2 ranges, MinIndex and MaxIndex (including)
    } ROI_PARAMETERSET, *P_ROI_PARAMETERSET;

    Note: The caller must always initialize member lSize to the size of the data structure
    """
    pass

# Data acquisition functions

def SDACQMP_GetSpectra() -> int:
    """
    Parameter:
    LONG l_ID (0...MAXINTERFACE)

    Return value:
    LONG (0=OK, -1=NOK = error level, -2=WNG = error level)

    Description:
    Function reads all available channel data from the board of the chosen
    interface and stores it to the allocated and mapped memory RawSpectral data.
    If DarkCurrentCorrectionMode is enabled (default) the RawData will
    be corrected by using the last stored DarkCurrentData of the same
    channel.

    The values in the buffer are the mean values of (average) measurement in energy counts covered by the pixel number.
    If the given parameter ‘l_ID’ is '0' the function requests a data acquisition of all enabled interfaces (see SDACQMP_SetInterfaceActive and
    SDACQMP_SetInterfaceInactive), otherwise only the specified interface is used.
    """
    pass

def SDACQMP_GetSpectraEx() -> int:
    """
    Parameter:
    LONG lWithShutterCtrl (0 = FALSE, 1 = TRUE)
    LONG l_ID (0...MAXINTERFACE)

    Return value:
    LONG (0=OK, -1=NOK = error level, -2=WNG = error level)

    Description:
    same as SDACQMP_GetSpectra() if lWithShutterCtrl = TRUE, but it’s
    possible to acquire data without the built-in mechanism for automatic
    shutter control (set lWithShutterCtrl to FALSE).
    """
    pass

def SDACQMP_GetDarkCurrent() -> int:
    """
    Parameter:
    LONG l_ID (0...MAXINTERFACE)

    Return value:
    LONG (0=OK, -1=NOK = error level, -2=WNG = error level)

    Description:
    Function reads all available channel data from the board of the selected interface and stores it to the allocated and mapped memory as
    DarkCurrentData.

    The values in the buffer are the mean values of (average) measurement in energy counts covered to the pixel number.
    If the given parameter ‘l_ID’ is '0' the function requests a data acquisition of all enabled interfaces (see SDACQMP_SetInterfaceActive and
    SDACQMP_SetInterfaceInactive), otherwise only the specified interface is used.
    Note: Dark current correction is enabled for all channels by default. All data acquisitions following the first dark current acquisition will therefore be performed with dark current
    correction engaged.
    """
    pass

def SDACQMP_GetDarkCurrentWithShutter() -> int:
    """
    Parameter:
    LONG l_delaytime (delay time in ms)
    LONG l_ID (0...MAXINTERFACE)

    Return value:
    LONG (0=OK, -1=NOK = error level, -2=WNG = error level)

    Description:
    Function starts dark current acquisition for the selected interface:
    1. Closes shutter (signal SHUT-EA / digital output #2) with
    the corresponding polarity, respectively closes the shutter
    of all initialized LS components of the specified interface
    2. Waits to finish the delay time
    3. Reads the sample values and stores data to the buffer
    4. Opens the shutter (signal SHUT-EA / digital output #2)
    with the corresponding polarity respectively opens the
    shutter of all initialized LS components of the specified interface
    5. Waits to finish the delay time
    Note: Dark current correction is enabled for all channels by default. All data acquisitions following the first dark current acquisitions will therefore be performed with dark current
    correction engaged.
    Note: The value ‘l_delaytime’ can be 0, if a LS component with automatic shutter control is
    used.
    If hardware flash mode is used, this function disables the hardware flash during
    the dark current data acquisition.
    """
    pass

def SDACQMP_GetBufferedSpectra() -> int:
    """
    Parameter:
    PLONG pl_AcquiredSpectra (Returns number of
    acquired spectra in buffer)
    PLONG pl_LostSpectra (Returns number of lost
    spectra)
    LONG l_ID (0...MAXINTERFACE)

    Return value:
    LONG (0=OK, -1=NOK = error level, -2=WNG = error level)

    Description:
    The function is only applicable to asynchronous buffered sensor work
    modes (i.e. GetBufferedScan). In addition to SDACQMP_GetSpectra
    it returns the number of already acquired and lost spectra.
    A warning of type WARNING_SPECBUFFER_OVERFLOW occurs,
    when the buffer is full. The number of lost spectra is returned in
    pl_LostSpectra.
    """
    pass

def SDACQMP_SetInterfaceActive() -> int:
    """
    Parameter:
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function enables the specified interface for the next global data ac
    quisition via function call of SDACQMP_GetSpectra or
    SDACQMP_GetDarkCurrent (only necessary if the interface was ex
    plicitely disabled via function call of SDACQMP_SetInterfaceInActive)
    """
    pass

def SDACQMP_SetInterfaceInActive() -> int:
    """
    Parameter:
    LONG l_ID (1...MAXINTERFACE)
    
    Return value:LONG (0 = OK, -1 = NOK = error level)
    
    Description:
    Function disables the specified interface for the next global data acquisition via function call of SDACQMP_GetSpectra or
    SDACQMP_GetDarkCurrent. After doing this the interface electronics
    is disabled until it will be explicitly enabled by the function call of
    SDACQMP_SetInterfaceActive
    """
    pass

# Digital I/O

def SDACQMP_IOSetDigOutput1() -> int:
    """
    Parameters:
    LONG l_level (true for high / false for low)
    LONG l_ID (1...MAXINTERFACE)
    
    Return value:
    LONG (0 = OK, -1 = NOK = error level)
    
    Description:
    Function sets the digital output #1 of the selected interface to the
    specified level.
    """
    pass

def SDACQMP_IOSetDigOutput2() -> int:
    """
    Parameters:
    LONG l_level (true for high / false for low)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function sets the digital output 2 of the selected interface to the specified level.

    Remarks:
    The function SDACQMP_GetDarkCurrentWithShutter() uses digital
    output #2 to control an external shutter.
    """
    pass

def SDACQMP_IOSetDigOutput3() -> int:
    """
    Parameters:
    LONG l_level (true for high / false for low)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function sets digital output #3 of the selected interface to the specified level.

    Remarks:
    PD-USB01: signal DO3 (since CPLD version 2.03, not available if DIN_DSUB is used)
    PD-PCI01V1: signal RES_OUT (not available if DIN_DSUB is used)
    PD-ETH01: signal DO3
    """
    pass

def SDACQMP_IOSetDigOutputs() -> int:
    """
    Parameters:
    LONG l_outputs (bit code:1 for high / 0 for low)
    LONG l_mask (bit code 1 sets selected output to the new level)
    LONG l_ID (1...MAXINTERFACE)
    
    Return value:
    LONG (0 = OK, -1 = NOK = error level)
    
    Description:
    Function sets the masked digital outputs of the selected interface to
    the specified level.
    """
    pass

def SDACQMP_IOGetDigInput1() -> int:
    """
    Parameters:
    PLONG pl_polarity (true for high / false for low)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function gets the current polarity from the digital input 1 of the selected interface.
    """
    pass

def SDACQMP_IOGetDigInput2() -> int:
    """
    Parameters:
    PLONG pl_polarity (true for high / false for low)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function gets the current polarity from the digital input 2 of the selected interface.
    """
    pass

def SDACQMP_IOGetDigInput3() -> int:
    """
    Parameters:
    PLONG pl_polarity (true for high / false for low)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function gets the current polarity from the digital input 3 of the selected interface.

    Remarks:
    PD-USB01: signal DI3 (since CPLD version 2.03, not available if
    DIN_DSUB is used)
    PD-PCI01V1: EXTRIG
    PD-ETH01: signal DI3
    """
    pass

def SDACQMP_IOGetDigInputs() -> int:
    """
    Parameters:
    PLONG pl_inputs (bit code:1 for high / 0 for low)
    LONG l_mask (bit code 1 read selected input)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function sets the masked digital outputs of the selected interface to
    the specified level.
    """

def SDACQMP_ParaSetInputSource() -> int:
    """
    Parameters:
    LONG l_InSource:
    - DIN_FEE (Default)
    - DIN_DSUB
    - DIN_AUX (PD_USB01)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Functions sets the kind of connector
    """
    pass
    
def SDACQMP_ParaSetInputLatchMode() -> int:
    """
    Parameters:
    LONG l_flags:
    Bit 0: 1 latch mode enabled for DIN1, 0 = disabled
    Bit 1: 1 latch mode enabled for DIN2, 0 = disabled
    Bit 2: 1 latch mode enabled for DIN3, 0 = disabled
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Functions sets the latch mode for the specified digital inputs (Default =
    disabled).
    
    Note:
    PD-PCI(e)01V1, PD-USB01V1: not available for DIN3.
    """
    pass
    
# Error information

def SDACQMP_GetErrorCode() -> int:
    """
    Parameters:
    P_LLERRORS p_errors (pointer to the structure LLERROR)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function fills the structure LLERROR with information about the last
    occurred error.

    Note:
    This code is only valid for the last function call which returned ‘NOK’
    """
    pass

def SDACQMP_WarningMessagesEx() -> int:
    """
    Parameters:
    LONG l_warnings (bitwise encoded warnings)
    All supported values (WNG_XXXX ) are defined in sdacq32_types.h
    LONG l_dialog (true=enables warning dialog box,
    false=disables warning dialog box)
    LONG l_ID (0...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function enables / disables warning functionality and enables / disables the warning dialog box
    Default: Most warnings are disabled
    The following warnings are implemented:
    1. AD-Converter overflow
    2. AD-Converter underflow (HR-FEE only)
    3. Overflow of spectra buffer (asynchronous sensor work
    modes, enabled by default)
    Use the AD warnings to detect too much light for the AD-Converter
    and adapting integration time.
    l_ID = 0: enable/disable warnings for all opened interfaces
    l_ID > 0: enable/disable warnings for one specific interface
    If at least one operating electronics or its driver does not support
    ‘warnings’ an error will occur.
    After the function has finished warnings are enabled for specified operating electronic(s) which driver(s) supports this.
    The parameter l_warnings specifies the warnings which are to be enabled. One or more of the flags WNG_XXXX can be combined
    (exception: WNG_DISABLE_ALL cannot be combined with any other
    flag).
    Note: This function is only useable if at least one operating electronics is opened!
    """
    pass

# Specific MUX functions

def SDACQMP_ParaSetMUXMode() -> int:
    """
    Parameters:
    LONG l_muxmode (defined in sdacq32_types.h)
    LONG l_channelnr (count of physical channels)
    (l_channelnr is ignored if parameter
    l_muxmode is NOT_AVAILABLE)
    LONG l_ID (1...MAXINTERFACE)
    
    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function sets the MUX mode and the quantity of physical channels, if necessary new initialization.
    Min: all MUX-Types 1
    Max: MUX-Type 4P: 4
    MUX-8A 8
    MUX-FSM 3/4/6/9/16
    MUX-O 3/4
    Attention! The function adapts the integration time to its actual minimum if it is
    too short. If ‘l_muxmode’ is ‘NOT_AVAILABLE’ the number of physical
    channels is set to the minimum (1), also the number of the current
    channels is set to 1.
    """
    pass

def SDACQMP_ParaSetMUXActiveChannel() -> int:
    """
    Parameters:
    LONG l_channelnr (number of active physical channel)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    In ‘Sequential Mode’ l_channelnr defines the currently active channel
    number, in ‘Simultaneous Mode’ l_channelnr specifies the number
    of currently active channels which can be between 1 to max. number
    which was defined with the routine SDACQMP_ParaSetMUXMode().
    Attention! The function adapts the integration time to its actual minimum if it is
    too short.
    """
    pass

# Specific data structure functions

def SDACQMP_AllocRawData() -> int:
    """
    Parameters:
    CHANNEL_ID *channel_ID (pointer to a internal memory location)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function allocates the memory for a channel and initializes its values.
    The output parameter ‘channel_ID’ is a pointer to its address. After doing this it is necessary to map this memory to a physical channel by
    using SDACQMP_ParaSetMapping.
    """
    pass

def SDACQMP_ParaSetMapping():
    """
    Parameters:
    CHANNEL_ID *channel_ID (channel identity, IN=0, OUT=xy)
    LONG l_channel (physical channel number 1...8)
    LONG l_ID (1...MAXINTERFACE)
    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function maps the allocated memory to a specified physical MUX
    channel, defined by the parameter ‘l_channel’ of the selected interface, defined by parameter ‘l_ID’.

    Note: SDACQMP_AllocRawData, SDACQMP_FreeRawData
    """
    pass

def SDACQMP_FreeRawData() -> int:
    """
    Parameters:
    CHANNEL_ID *channel_ID (channel identity)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function frees the allocated memory for specified channel.
    The in-/output parameter ‘channel_ID’ is a pointer to its address. After
    running this function ‘channel_ID’ is NULL and all data are lost.
    """
    pass

# Misc functions for additional components

# LS control
# Note: These functions are only available if a separate LS cassette or LS flash lamp is connected to the I²C bus of the interface electronics.

def SDACQMP_LS_Initialize() -> int:
    """
    Parameters:
    LONG l_IF_ID (1...MAXINTERFACE)
    LONG l_LS_ID (Default = 1)
    LONG l_dummy (must be “0”, not used)
    PLONG pl_result (OUT: available lamps)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Opens and initializes the LS cassette and returns to ‘pl_result’ the
    found LS type (constants are defined in sdacq32_types.h)
    LS_HAL_ONLY = 0x01: LS lamp 1 (Halogen) is available
    LS_D2_ONLY = 0x02: LS lamp 2 (Deuterium) is available
    LS_HAL_AND_D2 = 0x03: LS lamp 1+2 (Halogen and
    Deuterium) are available
    LS_FLASH = 0x04: LS flash lamp is available
    """
    pass

def SDACQMP_LS_OpenShutter() -> int:
    """
    (only available for LS cassette)
    Parameters:
    LONG l_IF_ID (1...MAXINTERFACE)
    LONG l_LS_ID (Default = 1)
    LONG l_timeout (0…5000ms, Default = 1000ms)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function opens the shutter of the specified component.
    ‘l_timeout’ of 0 (no timeout) opens the shutter without
    checking for successful operation and returns immediately after setting its digtal output.
    """
    pass

def SDACQMP_LS_CloseShutter() -> int:
    """
    (only available for LS cassette)

    Parameters:
    LONG l_IF_ID (1...MAXINTERFACE)
    LONG l_LS_ID (Default = 1)
    LONG l_timeout (0…5000ms, Default = 1000ms)

    Return value:
    LONG (0 = OK, 1 = NOK = error level)

    Description:
    Function closes the shutter of the specified component.
    ‘l_timeout’ of 0 (no timeout) opens the shutter without checking for
    successful operation and returns immediately after setting its digital
    output.
    """
    pass

def SDACQMP_LS_PowerON() -> int:
    """
    (only available for LS cassette)

    Parameters:
    LONG l_IF_ID (1...MAXINTERFACE)
    LONG l_LS_ID (Default = 1)
    LONG l_LS (0x01= Hal, 0x02 = D2, 0x03 = both)
    LONG l_timeout (0…120000ms, Default = 80000ms)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function turns on the selected light sources.
    ‘l_timeout’ of 0 (no timeout) turns on the selected light source(s) without checking for successful operation and returns immediately after
    setting its digital output(s).
    """
    pass
    
def SDACQMP_LS_PowerOFF() -> int:
    """
    (only available for LS cassette)

    Parameters:
    LONG l_IF_ID (1...MAXINTERFACE)
    LONG l_LS_ID (Default = 1)
    LONG l_LS (0x01= Hal, 0x02 = D2, 0x03 = both)
    LONG l_timeout (0…120000ms, Default = 80000ms)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function turns off the selected light sources.
    ‘l_timeout’ of 0 (no timeout) turns off the selected light soure(s) withoutchecking for successful operation and returns immediately after
    setting its digital output(s).
    """
    pass

def SDACQMP_LS_GetShutterPosition() -> int:
    """
    (only available for LS cassette)

    Parameters:
    LONG l_IF_ID (1...MAXINTERFACE)
    LONG l_LS_ID (Default = 1)
    PLONG pl_position (OUT: 1=Opened, 0=Closed)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function returns to ‘pl_position’ the actual position of
    the specified shutter.
    """
    pass

def SDACQMP_LS_GetStatus() -> int:
    """
    (only available for LS cassette)

    Parameters:
    LONG l_IF_ID (1...MAXINTERFACE)
    LONG l_LS_ID (Default = 1)
    PLONG pl_status (OUT: status byte)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function returns the status of the specified LS component which is
    encoded as follows:
    LS cassette:
    Bit 0: status D2 (0 = On, 1 = Off)
    Bit 1: status Hal (0 = On, 1 = Off)
    Bit 2: status shutter (0 = OK, 1 = error)
    Bit 3: temperature limit (0 = OK, 1 = temp > max)
    Bit 4: shutter position (0 = Closed, 1 = Opened)
    Bit 5: control status Shutter (0 = Close, 1 = Open)
    Bit 6: control status Hal (0 = On, 1 = Off)
    Bit 7: control status D2 (0 = On, 1 = Off)
    The bits 5-7 represent the target state the specific device should have
    if no error occurred. This does not necessarily reflect the current state
    of the device. In order to check the actual current status compare its
    bits with the corresponding bits 0-2. Note that the bits have negative
    logic.
    LS flash: Bit 8: parameterizing mode (0=manually, 1=remote)
    """
    pass

def SDACQMP_LS_GetActualTemperature() -> int:
    """
    (only available for LS cassette)
    Parameters:
    LONG l_IF_ID (1...MAXINTERFACE)
    LONG l_LS_ID (Default = 1)
    PLONGpl_temperature (OUT: temperature in °C)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function returns to ‘pl_temperature’ the actual temperature in the
    specified LS cassette.
    """
    pass

def SDACQMP_LS_SetTemperatureAlarm() -> int:
    """
    (only available for LS flash)
    Parameters:
    LONG l_IF_ID (1...MAXINTERFACE)
    LONG l_LS_ID (Default = 1)
    LONG l_Tos (Default = 80 = 80°C)
    LONG l_Thyst (Default = 5 = 5°C)

    Return value:
    LONG (0 = OK, 1 = NOK = error level)

    Description:
    Function sets the programmable limit for Overtemperature Shutdown.
    The temperature at which the alarm condition goes off is the result of
    ‘l_Tos’ – ‘l_Thyst’.
    Without using this function the overtemperature shutdown is active if
    the temperature in the LS cassette exeeds 80°C and it goes off if the
    cassette is cooled down to 75°C.
    """
    pass

def SDACQMP_LS_ReadFlashRate() -> int:
    """
    (only available for LS flash)

    Parameters:
    LONG l_IF_ID (1...MAXINTERFACE)
    LONG l_LS_ID (Default = 1)
    PLONG pl_flashrate (current value in [ms])

    Return value:
    LONG (0 = OK, -1 = NOK = error level)
    
    Description:
    Function returns to ‘pl_flashrate’ the flash rate from the LS flash component in [ms]
    """
    pass
    
def SDACQMP_LS_SetFlashCounter() -> int:
    """
    (only available for LS flash)

    Parameters:
    LONG l_IF_ID (1...MAXINTERFACE)
    LONG l_LS_ID (Default = 1)
    LONG l_counter (1 - l_counter - 254)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function sets the number of flashes during a spectral data acquisition.
    The time interval between two flashes is constant and can be read out
    using the function ‘SDACQMP_LS_ReadFlashRate’
    """
    pass
    
def SDACQMP_LS_GetRemoteStatus() -> int:
    """
    (only available for LS flash)

    Parameters:
    LONG l_IF_ID (1...MAXINTERFACE)
    LONG l_LS_ID (Default = 1)
    PLONG pl_rem_status

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function returns to ‘pl_rem_status’ the parameterizing mode (defined
    in sdacq32_types.h):
    LS_FLASH_STATE_MANUALLY: no software access to LS flash
    LS_FLASH_STATE_REMOTE: remote (Default)
    """
    pass

def SDACQMP_LS_SavePowerStatus() -> int:
    """
    (only available for LS-V2)
    Parameters:
    LONG l_IF_ID (1...MAXINTERFACE)
    LONG l_LS_ID (Default = 1)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function saves the current power status to the light source, so that
    this status is the new default status.
    These functions allow to set or get defined LS properties of a light source. If the selected property is
    not supported for the used LS type the function fails with an error.
    Errorlevel = FUNCTION_CALL_IGNORED
    Errorcode = FUNCTION_NOT_AVAILABLE
    Errorinfo = FUNCTION_NOT_SUPPORTED
    """
    pass

def SDACQMP_LS_GetSTRProperty() -> int:
    """
    Parameters:
    LONG l_IF_ID (1...MAXINTERFACE)
    LONG l_LS_ID (Default = 1)
    LS_Property lPropertyID defined in LS_Property
    LONG lSize buffer size
    char* pucValue pointer to a string buffer

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Gets a string value for the selected LS property.
    """
    pass
    
def SDACQMP_LS_GetLNGProperty() -> int:
    """
    Parameters:
    LONG l_IF_ID (1...MAXINTERFACE)
    LONG l_LS_ID (Default = 1)
    LS_Property lPropertyID defined in LS_Property
    PLONG plValue

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Gets a long value for the selected LS property.
    """
    pass
    
def SDACQMP_LS_SetLNGProperty() -> int:
    """
    Parameters:
    LONG l_IF_ID (1...MAXINTERFACE)
    LONG l_LS_ID (Default = 1)
    LS_Property lPropertyID defined in LS_Property
    LONG lValue

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Sets a long value for the selected LS property.
    """
    pass
    
def SDACQMP_LS_GetDBLProperty() -> int:
    """
    Parameters:
    LONG l_IF_ID (1...MAXINTERFACE)
    LONG l_LS_ID (Default = 1)
    LS_Property lPropertyID defined in LS_Property
    PDOUBLE pdValue

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Gets a double value for the selected LS property.
    """
    pass

def SDACQMP_LS_SetDBLProperty() -> int:
    """
    Parameters:
    LONG l_IF_ID (1...MAXINTERFACE)
    LONG l_LS_ID (Default = 1)
    LS_Property lPropertyID defined in LS_Property
    DOUBLE dValue
    
    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Sets a double value for the selected LS property.
    """
    pass


# LS Properties
# Note:
# Properties are currently supported for the following LS types:
# - BEK-Laser
# - BEK-HMP
# Different LS types support different properties. Some of them are read-only or only
# writeable. The availability and the R/W attribute depend on LS type, firmware version
# or libraries version.

# |ID | Type | Description
# LS_PROP_FW_VERSION | string | firmware version
# LS_PROP_FW_DATE string date of firmware version
# LS_PROP_LS_FAM string family name
# LS_PROP_LS_TYPE string type name
# LS_PROP_LS_ASSEMB string assembly name
# LS_PROP_SERIAL_NUMBER long/string serial number
# LS_PROP_OP_HOURS_SEC long system operating time [sec]
# LS_PROP_OP_HOURS_WNG_SEC long operating time warning limit [sec]
# LS_PROP_INTERLOCK_MASK (BEK Laser) long interlock mask (Bit0…4)
# LS_PROP_INTERLOCK_NO (BEK Laser) long interlock number
# LS_PROP_RELEASE_INTERLOCK (BEK Laser) long release interlock
# LS_PROP_NOMINAL_CONDITION_OF_POWER_STATUS (BEK Laser) long 1 = Power On, 0 = Power Off
# LS_PROP_COM_INTERFACE long/string 1=I²C, 2= serial “I²C”, “serial”
# LS_PROP_OP_HOURS_MIN long System operating time [min]
# LS_PROP_AVAIL_LS long Bit0 = LS1, Bit1 = LS2
# LS_PROP_OP_HOURS1 long operating time LS1[hours]
# LS_PROP_OP_HOURS2 long operating time LS2[hours]
# LS_PROP_OP_HOURS_WNG1 long operating time LS1[hours]
# LS_PROP_OP_HOURS_WNG2 long operating time LS2[hours]
# LS_PROP_TEMPERATURE double/string LS temperature
# LS_PROP_SHUTTER_POSITION long Open = 1, Closed = 0
# LS_PROP_DEFECT_LAMPS long Bit0 = LS1, Bit1 = LS2 1 = defact, 0 = ok
# LS_PROP_STATUS long LS status bits
# LS_PROP_REDUNDANCY long redundant LS type True = 1, False = 0
# LS_PROP_ACTIVE_LS long Switch active LS Bit0 = LS1, Bit1 = LS2
# LS_PROP_IS_DEFECT_MESSAGE_SUPPORTED long LS is able to transmit a defect message in case of a lamp blackout True = 1, False = 0
# LS_PROP_AUTOMESSAGE long enables/disables defect message Enable(d) = 1, Disable(d) = 0
# LS_PROP_IS_DEFECT_MESSAGE_RECEIVED long LS transmitted a blackout message True = 1, Fals = 0
# LS_PROP_DEFECT_MESSAGE_RESULT long 1 = LS1, 2 = LS2
# LS_PROP_COM_PORT long/string Used comport number x/ “COMx”
# LS_TIMEOUT_SHUTTER long Timeout Shutter[sec]
# LS_TIMEOUT_LS1 long Timeout LS1[sec]
# LS_TIMEOUT_LS2 long Timeout LS2[sec]
# LS_PROP_ACTIVE_RED_LS long Switch active LS of a redundant LS type Bit0 = LS1, Bit1 = LS2
# LS_PROP_LASER_CENTR_WAVE_LENGTH Double/string Center wave length [nm] “#.### nm”


def SDACQMP_HWConfig_ChangeLSParams() -> int:
    """
    Parameters:
    LONG lLSType (Default = LS_FAM_BEKHMP)
    LONG lPort (Com Port 1…x, 0 = delete information)
    LONG lFlags (Default = 0)
    LONG lChannels (Channel number 0…16)
    LONG l_IF_ID (1...MAXINTERFACE)
    LONG l_LS_ID (Default = 1)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function sets the access parameter of a light source.
    """
    pass

def SDACQMP_HWConfig_GetLSParams() -> int:
    """
    Parameters:
    LONG plLSType (LS_FAM_BEKHMP = 0x09)
    LONG plPort Com Port 1…x)
    LONG plFlags (Default = 0)
    LONG plChannels (Channel number 0…16)
    LONG l_IF_ID (1...MAXINTERFACE)
    LONG l_LS_ID (Default = 1)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function gets the access parameter of a light source.

    Note:
    The com port number depends on the used com port of the PC. If you transfer hardand software to another PC usually the new com port number has to be defined before
    start to communicate with the tec5 hardware.
    """
    pass

# Data access functions

def SDACQMP_GetStoredRawData() -> int:
    """
    Parameters:
    CHANNEL_ID channel_ID (channel identity)
    PDOUBLE p_data[] (pointer to an double array)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function copies the specified Raw Data to the address range pointed
    to by ‘p_data’. The allocated memory must be large enough to accommodate the size of one scan. The data amount is equal to the
    number of pixels of the sensor (sensor length, for CCD 2D operation
    multiplied by number of binning areas). Most configurations and sensor types size do not exceed 2048 pixels.
    """
    pass

def SDACQMP_GetStoredRawDataBurst() -> int:
    """
    Parameters:
    CHANNEL_ID channel_ID (channel identity)
    LONG l_index (1…l_burst)
    PDOUBLE p_data[ ] (pointer to an double array)
    
    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function copies one specified RawData spectra to the address range
    pointed to by ‘p_data’. The data amount is equal to the number of pixels of the sensor (sensor length, for CCD 2D operation multiplied by
    number of binning areas). Most configurations and sensor types size
    do not exceed 2048 pixels.
    The maximum value of ‘l_index’ is equal to the ‘l_burst’ value which is
    set with the function SDACQMP_ParaSetBurstNumber before calling
    SDACQMP_GetSpectra. The actual value of “l_burst” for a specified
    channel is accessible by using the function
    SDACQMP_GetStoredBurstNumber
    """
    pass

def SDACQMP_GetStoredPixelnumber() -> int:
    """
    Parameters:
    CHANNEL_ID *channel_ID (channel identity)
    PDOUBLE p_data[ ] (pointer to an double array)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function copies the specified pixel number to
    the address range pointed to by ‘p_data’. The data amount is equal to the
    number of pixels of the sensor (sensor length, for CCD 2D operation multiplied
    by number of binning areas). Most configurations and sensor type’s size do
    not exceed 2048 pixels.
    """
    pass

def SDACQMP_GetStoredDarkcurrentData() -> int:
    """
    Parameters:
    CHANNEL_ID *channel_ID (channel identity)
    PDOUBLE p_data[ ] (pointer to an double array)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function copies the specified dark current data to the address range
    beginning with the pointer ‘p_data’. The data amount is equal to the
    number of pixels of the sensor (sensor length, for CCD 2D operation
    multiplied by number of binning areas). Most configurations and sensor types size do not exceed 2048 pixels.
    """
    pass

def SDACQMP_DeleteDarkcurrentData() -> int:
    """
    Parameters:
    CHANNEL_ID *channel_ID (channel identity)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function deletes the specified DarkCurrentData (set to 0)
    """
    pass

def SDACQMP_GetStoredDarkModeSettings() -> int:
    """
    Parameters:
    CHANNEL_ID *channel_ID (channel identity)
    PLONG l_darkcorr_done (true if dark current correction is
    done, false else)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function sets l_darkcorr_done to true if dark current correction of the
    specified channel is done.
    """
    pass

def SDACQMP_GetStoredAverageNumber() -> int:
    """
    Parameters:
    CHANNEL_ID *channel_ID (channel identity)
    PLONG pl_average (average number)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function gets the average number which was used by
    SDACQMP_GetSpectra or SDACQMP_GetDarkCurrent of the specified channel.
    """
    pass

def SDACQMP_GetStoredBurstNumber() -> int:
    """
    Parameters:
    CHANNEL_ID *channel_ID (channel identity)
    PLONG pl_burst (burst number)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function gets the burst number which was used by
    SDACQMP_GetSpectra or SDACQMP_GetDarkCurrent of the specified channel.
    """
    pass

def SDACQMP_GetStoredIntegrationtime() -> int:
    """
    Parameters:
    CHANNEL_ID *channel_ID (channel identity)
    PDOUBLE pd_integrationtime (integration time)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function gets the integration time which was used by the last call of
    SDACQMP_GetDarkCurrent or SDACQMP_GetSpectra of the specified channel.
    """
    pass

def SDACQMP_GetStoredTimeStamp() -> int:
    """
    Parameters:
    CHANNEL_ID *channel_ID (channel identity)
    LONG l_Index (Default = 1, Burst: 1…n)
    PLONG pl_Counter (PD_ETH01: internal spectrum counter,
    Default: NULL = not used)
    P_TIMEDATE_EXT timedate (a structure defined
    in sdacq32_types.h, NULL = not used)
    PLONGLONG pllTimeStampRelative_us (Default: NULL = not used)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function gets the stored system time which was valid at the last call of
    SDACQMP_GetDarkCurrent or SDACQMP_GetSpectra of the
    specfied channel.
    """
    pass

def SDACQMP_GetStoredIntensity() -> int:
    """
    Parameters:
    CHANNEL_ID *channel_ID (channel identity)
    PDOUBLE pd_MinCounts (min. intensity in counts)
    PDOUBLE pd_MaxCounts (max. intensity in counts)
    PDOUBLE pd_MinPercent (min. intensity as percentage)
    PDOUBLE pd_MaxPercent (max. intensity as percentage)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Functions gets the stored intensity (before dark current correction)
    of the last data acquisition.Non used parameters can be NULL.
    """
    pass

# Hardware configuration functions

def SDACQMP_HWConfig_GetSensorParamsEx2() -> int:
    """
    Parameters:
    LONG l_Resered (must be 0, for later use)
    P_SENSORPARAMS_X pspda (result structure)
    LONG l_channel (1…MAX_CHANNEL_NUMBER)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function copies the sensor parameters specified by ‘l_channel’ from
    EEPROM of FEE or MUX to a SENSORPARAMS_X structure.
    The sensor coefficients are stored as single precision floating point
    values although the data type of the structure SENSORCOEFFS_X is
    a double precision floating point value.
    """
    pass

def SDACQMP_HWConfig_ChangeSensorParamsEx2() -> int:
    """
    Parameters:
    LONG l_Resered (must be 0, for later use)
    P_SENSORPARAMS_X pspda (result structure)
    LONG l_channel (1…MAX_CHANNEL_NUMBER)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function overwrites the stored sensor parameters specified by
    ‘l_channel’ in the EEPROM of FEE or MUX with the values in the
    SENSORPARAMS_X structure.
    The coefficients will be converted to single precision floating point values before writing them to the EEPROM.
    The settings will be active from the next call of
    SDACQMP_OpenOperationElectronicsDevice() on only
    """
    pass

# typedef struct _SENSORPARAMS_X
# {
# long lSize; // (INPUT / OUTPUT), size of structure
# SENSORCONFIG_X scfConfig;
# long lReserved; // must be 0
# SENSORCOEFFS_X scoCoeffs;
# } SENSORPARAMS_X, *P_SENSORPARAMS_X;
# typedef struct _SENSORCONFIG_X
# {
# short sSensorType; // sensor type
# short sSensorLength; // number of pixel
# short sSensorBinAreas; // for CCD sensors only, Def. = 1
# short sSensorPhysRows; // for CCD sensors only, Def. = 1
# } SENSORCONFIG_X, *P_SENSORCONFIG_X;
# typedef struct _SENSORCOEFFS_X
# {
# double dC0;
# double dC1;
# double dC2;
# double dC3;
# double dC4;
# } SENSORCOEFFS_X, *P_SENSORCOEFFS_X;
# Note: The caller must always initialize member lSize to the size of the data structure.

def SDACQMP_HWConfig_ParaGetHWConfigurationEx2() -> int:
    """
    Parameters:
    LONG l_Reserved (must be 0, for later use)
    P_HWSETTINGS_X phwsdata (result structure)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (>=0 = OK, <0 = NOK)

    Description:
    This function reads the configuration information from the hardware
    and fills the structure HWSETTINGS_X by using the same constants
    defined in ‘sdacq32_types.h’.
    """
    pass

# typedef struct _HWSETTINGS_X
# {
# long lSize; // (INPUT / OUTPUT), size of structure
# short sIFType; // (OUTPUT)
# short sFEEType; // (OUTPUT)
# short sMUXType; // (OUTPUT)
# short sNumSensorChannels; // (OUTPUT)
# long lReserved; // must be 0
# SENSORCONFIG_X scSensor[16]; // (OUTPUT)
# } HWSETTINGS_X, *P_HWSETTINGS_X;
# typedef struct _SENSORCONFIG_X
# {
# short sSensorType; // sensor type
# short sSensorLength; // number of pixel
# short sSensorBinAreas; // for CCD sensors only, Def. = 1
# short sSensorPhysRows; // for CCD sensors only, Def. = 1
# } SENSORCONFIG_X, *P_SENSORCONFIG_X;
# Note: The caller must always initialize member lSize to the size of the data structure


def SDACQMP_HWConfig_ChangeMUXParams() -> int:
    """
    Parameters:
    LONG l_MUXType (defined in sdacq32_types.h)
    LONG l_port (COM port for MUX-FSx control,
    1 for COM1)
    LONG l_assembly (defined in sdacq32_types.h)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)
    
    Description:
    Function writes the MUX-FSx parameters to the current operating
    electronics EEPROM, so that MUX-FSx can be controlled automatically by SDACQ32MP.DLL after the operating electronics is successfully
    initialized.

    Note: To delete these entries in the operating electronics and deactivate
    MUX-FSx control by SDACQ32MP.DLL set the parameter
    ‘l_MUXType’ to 0.
    """
    pass

def SDACQMP_HWConfig_GetMUXParams() -> int:
    """
    Parameters:
    PLONG pl_MUXType (defined in sdacq32_types.h)
    PLONG pl_port (COM port for MUX.FSM control, 1 for COM1)
    PLONG pl_assembly (defined in sdacq32_types.h)
    PLONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Function reads out the MUX-FSx parameters from the operation electronics EEPROM. The functions fails if no MUX-FSx was configured
    before or the MUX-FSx parameters were already deleted.
    """
    pass

# I2C components functions

def SDACQMP_I2C_Write_1() -> int:
    """
    Parameters:
    LONG l_device_address (1...256)
    UNSIGNED CHAR *puc_wbuf, (pointer to a string with max. 8 characters (Bytes))
    LONG l_bytes (number of Bytes 1...8)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    This function writes n (1<=n<=8) bytes to the I2C-Device with address
    ‘l_device_address’. For example, it can be used to write a bit pattern
    sequence to an I/O-Expander device.
    """
    pass

def SDACQMP_I2C_Read_1() -> int:
    """
    Parameters:
    LONG l_device_address (1...256)
    UNSIGNED CHAR *puc_rbuf, (pointer to a string with max. 8 characters (Bytes))
    LONG l_bytes (number of Bytes 1...8)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    This function reads n (1<=n<=8) bytes from the I2C-Device with address ‘l_device_address’. For example, it can be used to read I/Osignal pattern from an I/O-Expander device.
    """
    pass

def SDACQMP_I2C_Write_N() -> int:
    """
    Parameters:
    LONG l_device_address (1...256)
    UNSIGNED CHAR *puc_wbuf, (pointer to a string
    with max. 8 characters (Bytes))
    LONG l_index (1...256)
    LONG l_bytes (number of Bytes 1...8)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    This function writes n (1<=n<=8) bytes to the I2C-Device with address
    ‘l_device_address’ starting from device internal address ‘l_index’. For
    example, it can be used to write data to an I2C-EEPROM device.
    """
    pass

def SDACQMP_I2C_Read_N() -> int:
    """
    Parameters:
    LONG l_device_address (1...256)
    UNSIGNED CHAR *puc_rbuf, (pointer to a string
    with max. 8 characters (Bytes))
    LONG l_index (1...256)
    LONG l_bytes (number of Bytes 1...8)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)
    Description: This function reads n (1<=n<=8) bytes from the I2C-Device with address ‘l_device_address’ starting from device internal address
    ‘l_index’. For example, it can be used to read data from an I2CEEPROM device
    """
    pass

def SDACQMP_I2C_Programming() -> int:
    """
    Parameters:
    LONG device_address (1...256)
    UNSIGNED CHAR *puc_wbuf, (pointer to a string
    with max. 8 characters (Bytes))
    LONG l_index (1...256)
    LONG l_bytes (number of Bytes 1...8)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    This function is able to program n (1<=n<=8) bytes to the I2C-Device
    with address ‘l_device_address’ starting from device internal address
    ‘l_index’.
    It writes the data into the device, waits until programming cycle is
    complete, reads back the data and compares it with the original data
    to be written.
    """
    pass

def SDACQMP_I2C_Read_EEPROM_CustData() -> int:
    """
    Parameters:
    LONG l_ElectronicsFamily
    (ELC_INTERFACE or ELC_FRONTEND)
    LONG lRes (must be “0”, not used)
    UNSIGNED CHAR *puc_rbuf, (pointer to a string
    with max. 8 characters (Bytes))
    LONG l_index (0…63)
    LONG l_bytes (number of Bytes 1...8)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    This function reads n (1<=n<=8) bytes from the EEPROM of the electronics starting from device internal address ‘l_index’. The maximum
    addressable EEPROM range is 64 Byte.
    """
    pass

def SDACQMP_I2C_Write_EEPROM_CustData() -> int:
    """
    Parameters:
    LONG l_ElectronicsFamily (ELC_INTERFACE or ELC_FRONTEND)
    LONG lRes (must be “0”, not used)
    UNSIGNED CHAR *puc_wbuf, (pointer to a string with max. 8 characters (Bytes))
    LONG l_index (0…63)
    LONG l_bytes (number of Bytes 1...8)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    This function writes n (1<=n<=8) bytes to the EEPROM of the electronics starting from device internal address ‘l_index’. The maximum
    addressable EEPROM range is 64 Byte.
    """
    pass

def SDACQMP_I2C_Read_EEPROM() -> int:
    """
    Parameters:
    LONG device_address (0...240)
    UNSIGNED CHAR *puc_rbuf, (pointer to a string with 256 characters (Bytes))
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    This function reads 256 bytes from an EEPROM. Note that addresses
    which are used from tec5 cannot be used for public purposes.
    """
    pass

def SDACQMP_I2C_Write_EEPROM() -> int:
    """
    Parameters:
    LONG device_address (0...240)
    UNSIGNED CHAR *puc_rbuf, (pointer to a string
    with 256 characters (Bytes))
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    This function reads 256 bytes from an EEPROM. Note that addresses
    which are used from tec5 cannot be used for public purposes.
    """
    pass

def SDACQMP_I2C_GetAllTemperatures() -> int:
    """
    Parameters:
    LONG l_reserved (should be 0)
    P_TEMPERATURE_RESULTS p_temperature_results
    (pointer to a instance of
    TEMPERATURE_RESULTS)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    This function retrieves all connected I2C temperature sensors (Max.=
    8 sensors) and copies their I2C addresses and their current
    temperature values to the given data struct.

    Note: Currently only supported for USB type electronics
    """
    pass

def SDACQMP_I2C_GetTemperature() -> int:
    """
    Parameters:
    LONG l_reserved, should be 0
    LONG l_index (0…7)
    FLOAT *pf_temperature (pointer to a
    float variable. The value is the temperature
    value in °C with a resolution of 0.01°)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    This function retrieves the current temperature of one specific
    temperature sensor. All available temperature sensors can be
    detected using the function “SDACQMP_I2C_GetAllTemperatures()”.
    It is recommended to use “SDACQMP_I2C_GetTemperature()” for
    a periodic refreshing and error handling.

    Note: Currently only supported for USB type electronics.
    """
    pass

# Linearization

def SDACQMP_Linearization() -> int:
    """
    Parameters:
    LONG l_Enable (TRUE / FALSE)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)

    Description:
    Enables the linearization for all currently mapped channels.
    The name of the linearization files must be the standard names
    which depends on the used sensor types.
    """
    pass

def SDACQMP_LinearizationChannel() -> int:
    """
    Parameters:
    CHANNEL_ID *channel_ID
    LONG l_Enable (TRUE / FALSE)
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    ???
    
    Description:
    Enables the linearization for one specified channel.
    The name of the linearization files must be the standard names
    which depends on the used sensor types.
    """
    pass

def SDACQMP_LinearizationChannelEx() -> int:
    """
    Parameters:
    CHANNEL_ID *channel_ID
    LONG l_Enable (TRUE / FALSE)
    PTCHAR pszFileName
    LONG l_ID (1...MAXINTERFACE)

    Return value:
    LONG (0 = OK, -1 = NOK = error level)
    
    Description:
    Enables the linearization for one specified channel with specified linearization file.

    Note: Before using one of the above functions make sure that the
    linearization file(s) „*.tlc“ (= tec5 linearization coefficients)
    which has been delivered from tec5 support are installed in the
    fixed path which is defined in the windows registry:

    Path: HKEY_CURRENT_USER\Software\\tec5\Application
    Value: DataPath
    Wert:
    Windows 7/8.x/10:
    “C:\Users\<Profile name>\AppData\Local\\tec5\Application”
    """
    pass

######################################################################
# Appendix A: Description of the Public Data Structures / Constants sdacq32_types.h

# INTERFACE types
PD_PCI01V1 = 4
PD_USB01 = 6
PD_ETH01 = 7
COE_USB11 = 9
PD_PCIE01 = 11
SEU_CGS = 12
DEFAULT_INTERFACECARD = PD_USB01

# // CONNECTOR for Digital input, SDACQMP_ParaSetInputSource()
DIN_FEE = 0 # (Default)
DIN_DSUB = 1
DIN_AUX = 3 # PD_USB01 only, since PLD version 2.03

# // FRONTEND types
FEE_HS = 3 # FEE high speed
FEE_HSMO = 6 # new, for Hamamatsu sensors
FEE_1M_NMOS = 9 # Fast FEE for NMOS
FEE_1M_NIR = 10 # Fast FEE for NIR
FEE_1M_CCD = 11 # Fast FEE for CCD
DEFAULT_FEETYPE = FEE_HS

# // MUX types
NO_MUX = 0
MUX_4P = 4
MUX_8A = 5
MUX_2OPT = 6
MUX_FSM = 7
MUX_O = 10
DEFAULT_MUXTYPE = NO_MUX

# // SENSOR types
SEN_PDA_HA_S390X = 0 # PDA NMOS Hamamatsu S390x
SEN_CCD_HA_S7030_4 = 7 # CCD Hamamatsu S-7030-4
SEN_CCD_HA_S7010_1 = 8 # CCD Hamamatsu S-7010-1
SEN_CCD_HA_S9840 = 23 # CCD Hamamatsu S-9840
SEN_CCD_HA_S11071 = 24 # CCD Hamamatsu S11071
SEN_CCD_HA_S1115X = 25 # CCD Hamamatsu S1115x
SEN_PDA_SU_LX_LD = 5 # PDA InGaAs SU LX / LD series
SEN_PDA_HA_G92XX = 13 # PDA InGaAs Hamamatsu G92xx
SEN_PDA_HA_G9212_14 = 21 # PDA InGaAs Hamamatsu G9212/14
SEN_PDA_JU_MB = 3 # PDA InGaAs Judson MB series
SEN_SS_CZ_MMS = 16 # Carl Zeiss MMS
SEN_SS_CZ_MMS_UV = 1 # Carl Zeiss MMS-UV
SEN_SS_CZ_MCS = 2 # Carl Zeiss MCS
SEN_SS_CZ_MCS_CCD = 17 # Carl Zeiss MCS-CCD
SEN_SS_CZ_CGS = 26 # Carl Zeiss CGS
SEN_SS_CZ_PGS_NIR_17_SUI = 14 # Carl Zeiss PGS-NIR 1.7 512SUI
SEN_SS_CZ_PGS_NIR_HM256 = 15 # Carl Zeiss PGS-NIR HM 256
SEN_SS_CZ_PGS_NIR_HM512 = 28 # Carl Zeiss PGS-NIR HM 512
SEN_SS_CZ_MMS_NIR_17 = 18 # Carl Zeiss MMS-NIR 1.7
SEN_SS_CZ_MMS_NIR_17_HR = 19 # Carl Zeiss MMS-NIR 1.7 HR
SEN_SS_CZ_MMS_NIR_17_JU = 20 # Carl Zeiss MMS-NIR 1.7 (Judson)
SEN_HEAD_HA_C806X = 10 # Hamamatsu Head C806x (InGaAs)
SEN_HEAD_HA_C7221 = 4 # Hamamatsu Head C7221 (InGaAs)
SEN_HEAD_HA_C702X = 9 # Hamamatsu Head C702x (CCD)
SEN_HEAD_HA_C704X = 6 # Hamamatsu Head C704x (CCD)
SEN_HEAD_HA_C5964 = 11 # Hamamatsu Head C5964 (NMOS)
SEN_GEN_XX_CFGFILE = 128 # Generic, defined by configuration file
DEFAULT_SENSORTYPE = SEN_PDA_HA_S390X

# SENSORLENGTH
PX128 = 128
PX256 = 256
PX512 = 512
PX532 = 532
PX1024 = 1024
PX1044 = 1044
PX2048 = 2048
PX2068 = 2068
PX2080 = 2080
DEFAULT_SENSORLENGTH = PX256

# MUX modes
NOT_AVAILABLE = 0
SEQUENTIELL = 1
SIMULTAN = 2
DEFAULT_MUXMODE = SEQUENTIELL

# channel numbers
CHANNEL_1 = 1
CHANNEL_2 = 2
CHANNEL_3 = 3
CHANNEL_4 = 4
CHANNEL_5 = 5
CHANNEL_6 = 6
CHANNEL_7 = 7
CHANNEL_8 = 8
MAX_CHANNEL_NUMBER = 8

# // MUX-FSM assemblies
MUX_FSM_3CH = 1
MUX_FSM_4CH = 2
MUX_FSM_6CH = 3
MUX_FSM_9CH = 4

# Average Count
DEFAULT_AVERAGE = 1

# Trigger Timeouttime
DEFAULT_TIMEOUTTIME = 60000

# // Shutter polarity
SHUTTER_POL_POSITIV = 0
SHUTTER_POL_NEGATIV = 1
DEFAULT_SHUTTER_POL = SHUTTER_POL_POSITIV
DEFAULT_CHANNEL_NUMBER = 1

# // sensor work modes
StartNewScanWithCleaning = 0x01
StartNewScanWithoutCleaning = 0x02
SyncToContScan = 0x03
ExternalTriggerSlope = 0x04
ExternalTriggerPulse = 0x05
GetLastScan = 0x06
GetBufferedScan = 0x07
ExternalTriggerSlopeWithCleaning = 0x08
ExternalTriggerPulseWithCleaning = 0x09
ExternalTriggerScanSlope = 0x0A
ExternalTriggerScanPulse = 0x0B
ExternalTriggerCycleSlope_WithCleaningSync = 0x0C
ExternalTriggerCyclePulse_WithCleaningSync = 0x0D
ExternalTriggerScanSlope_Buffered = 0x30
ExternalTriggerScanPulse_Buffered = 0x31
ExternalTriggerCycleSlope_Buffered = 0x32
ExternalTriggerCyclePulse_Buffered = 0x33
DEFAULT_SENSOR_WORK_MODE = SyncToContScan

# // sensor work mode flags
SWM_SUPPRESS_ERROR_MESSAGES = 0x01
SWM_SUPPRESS_FIFO_OVERFLOW_PROT = 0x02
SWM_ENABLE_EXTTRIG_READY_SIGNAL = 0x04
SWM_ENABLE_SPEC_GATE_INPUT = 0x08
SWM_ENABLE_EXTTRIG_RISING_EDGE = 0x10
SWM_ENABLE_ACQSTAT_SOMAA = 0x20

# // Global Type definitions
# typedef double *PDOUBLE; // pointer to double value
# typedef long CHANNEL_ID; // pointer to allocated data // mm / 02.10.98
# typedef struct _LLERROR // LL means low level
# {
# long l_errorlevel; // error level
# long l_errorcode; // error code
# char str_func_name[50]; // function name
# long l_errorinfo; // additional error information
# long l_IF_number; // actual interface number (by MOE_V1 equal to
# // MOE_ID, not used if only one interface is used
# // (SDACQ32)
# } LLERROR, *P_LLERROR;
# typedef struct /*td*/ { // Time / Date structure
# unsigned short usec // usecond
# unsigned short msec // msecond
# unsigned short sec; // second
# unsigned short min; // minute
# unsigned short hour; // hour
# unsigned short day; // day
# unsigned short month; // month
# unsigned short year; // year
# } TIMEDATE_EXT, *P_TIMEDATE_EXT;

# typedef struct _P_ROI_PARAMETERSET
# {
# long lSize; // size of struct [number of bytes]
# long lVersion; // must be 0
# unsigned short usROI[2][2]; // 2 ranges, MinIndex and MaxIndex (included)
# } ROI_PARAMETERSET, *P_ROI_PARAMETERSET;
# typedef struct _SENSORCONFIG_X
# {
# short sSensorType; // sensor type
# short sSensorLength; // number of pixel
# short sSensorBinAreas; // CCD sensor only, Def. = 1
# short sSensorPhysRows; // CCD sensor only, Def. = 1
# } SENSORCONFIG_X, *P_SENSORCONFIG_X;
# typedef struct _SENSORCOEFFS_X
# {
# double dC0; // wavelength cooefficients C0’..C4’
# double dC1;
# double dC2;
# double dC3;
# double dC4;
# } SENSORCOEFFS_X, *P_SENSORCOEFFS_X;
# typedef struct _SENSORPARAMS_X
# {
# long lSize; // size of SENSORPARAMS_X structure
# SENSORCONFIG_X scfConfig;
# long lReserved; // for later use, must be 0
# SENSORCOEFFS_X scoCoeffs;
# } SENSORPARAMS_X, *P_SENSORPARAMS_X;
# typedef struct _HWSETTINGS_X
# {
# long lSize; // size of HWSETTINGS_X structure
# short sIFType; // interface type
# short sFEEType; // frontend electronic type
# short sMUXType; // multiplexer type
# short sNumSensorChannels; // number of sensors (1...MAX_CHANNEL_NUMBER(MUX))
# long lReserved; // for later use, must be 0
# SENSORCONFIG_X scSensor[16];
# } HWSETTINGS_X, *P_HWSETTINGS_X;

# // Warnings
# #define WNG_DISABLE_ALL 0x00
# #define WNG_ADC_OVERFLOW 0x01 // Default: disabled
# #define WNG_SPEC_BUFFER_OVERFLOW 0x02 // Default: enabled
# #define WNG_FIFO_OVERFLOW 0x04
# #define LS_DEF_TIMEOUT_LAMPS 80000 // 80 sec (D2)
# #define LS_DEF_TIMEOUT_SHUTTER 1000 // 1 sec
# #define LS_HAL_ONLY 0x01
# #define LS_D2_ONLY 0x02
# #define LS_HAL_AND_D2 0x03
# #define LS_FLASH 0x04
# #define LS_FLASH_STATE_MANUALLY 0x00
# #define LS_FLASH_STATE_REMOTE 0x01
# // shutter control mode
# #define SCM_DEFAULT_OPEN 0x00
# #define SCM_DEFAULT_CLOSED 0x01
# #define SCM_DEFAULT_OPEN_V1 0x02
# #define SCM_DEFAULT_MODE SCM_DEFAULT_OPEN
# #endif

######################################################################

# Appendix B: Error Codes and Additional Error Information
# // sdacq32_error_codes.h

# //GENERAL CONSTANTS
#define ERRORTABLE
OK = 0
NOK = -1
WNG = -2

# //ERROR LEVELS
HARDWARE_ERROR_FROM_DRIVER = 1
MEMORY_ERROR = 2
DEVICE_ERROR = 3
FUNCTION_CALL_NOT_CORRECTLY_DONE = 4 # function partly done
FUNCTION_CALL_IGNORED = 5 # no effect, nothing is done
FUNCTION_CALL_EXECUTED_WITH_DEFAULT_VALUE = 6 # executed with default values ok
FUNCTION_CALL_EXECUTED_WITH_CORRECTED_VALUE = 7 # executed with Corrected values ok
WARNING_DACQ_CONTAINS_INVALID_PIXEL_DATA = 50 # ADC Over-/Underflow
WARNING_SPECTRAL_DATA_LOST = 51

# //ERROR CODES
# LEVEL 1: DRIVER ERRORS NOT USED ON THIS LEVEL
DACQERROR_RAS_FIFOEMPTY = 101
DACQERROR_TIMEOUT_RWS_NODATA = 102
DACQERROR_SYNC_WORD1 = 103
DACQERROR_SYNC_WORD2 = 104
DACQERROR_WORD3XX = 105
DACQERROR_SYNC_FIFI_NOTEMPTY = 106
DACQERROR_TIMEOUT_EOS_SCAN = 107
DACQERROR_TIMEOUT_EOS_DUMMYSCAN = 108
DACQERROR_ADR_CONTROL = 109
DACQERROR_FIFO_FULL = 110
DACQERROR_INTERRUPTS_NOT_SUCCESSFULL = 111
DACQERROR_INTERRUPTS_ALLWAYS_SET = 112
DACQERROR_TIMEOUT_EXT_TRIGG = 113
DRVERROR_COMMUNICATION_TIMEOUT = 140
DRVERROR_COMMUNICATION_DATASTREAM = 141
DRVERROR_DEVICE_REMOVED = 142
DRVERROR_SENSOR_NOT_AVAILABLE = 143
DRVERROR_FEE_NOT_AVAILABLE = 144
DRVERROR_FIFO_OVERFLOW = 145
DRVERROR_COMMUNICATION_INCOMPLETE_DATA = 146
DRVERROR_FIFOSIZE_INSUFFICIENT = 147
DRVERROR_POWER_FAILURE = 148
DACQERROR_SENSORWORKMODE_NOTAVAILABLE = 150
DACQERROR_WRONG_SENSOR_WORK_MODE = 151
DACQERROR_IO_NOT_AVAILABLE = 152
DRVERROR_FALSE_DRIVER_DATA_STRUCT = 153
DRVERROR_BURSTBUFFER_TO_SMALL = 154
DRVERROR_DEVICE_IS_STOPPED = 155
DRVERROR_FIRMWARE_DONTSUPPORT_FUNCTION = 156
DRVERROR_MEMORY_ALLOCATION = 157
DRVERROR_BUFFER_OVERFLOW = 158
DRVERROR_SPECTRA_NOTAVAILABLE = 159
ERR_I2C_NOCONTROLLER = 161
ERR_I2C_CONTROLLER_NOTINIT = 162
ERR_I2C_CONTROLLER_BUSY = 163
ERR_I2C_CONTROLLER_TRANSMISSION = 164
ERR_I2C_CONTROLLER_NOACKNOW = 165
ERR_I2C_PROGRAMMING_COMPARE = 166
ISPERR_XFVBUFFER_TO_SMALL = 171
ISPERR_PROGRAMMINGABORT = 172

# WARNINGS
WARNING_FIFO_FULL = 194
WARNING_FIFO_OVERFLOW = 195
WARNING_SPECBUFFER_OVERFLOW = 196
WARNING_GETSCANSYNCHRON_FIFO_NOT_EMPTY = 197
WARNING_ADC_UNDERFLOW = 198
WARNING_ADC_OVERFLOW = 199

# //LEVEL 2
NOT_ABLE_TO_ALLOC_MEMORY = 201
NOT_ABLE_TO_FREE_MEMORY = 202
NOT_ABLE_TO_LOCK_MEMORY = 203
NOT_ABLE_TO_UNLOCK_MEMORY = 204
NOT_ABLE_TO_REALLOC_MEMORY = 205
NOT_ABLE_TO_RELOCK_MEMORY = 206

# //LEVEL 3
NOT_ABLE_TO_OPEN_DEVICE = 301
NOT_ABLE_TO_CLOSE_DEVICE = 302
DEVICE_IO_NOT_SUCCESS = 303
NOT_ABLE_TO_OPEN_REGISTRY = 305
I2C_PROTECTED_AREA = 306
I2C_ERROR_WRITE_DATA = 307
I2C_ERROR_READ_DATA = 308
ACQ_THREAD_ERROR = 309
FIRMWARE_OR_DRIVER_DONT_SUPPORT_FUNCTION = 310
LOADING_CONFIGURATION_FILE_FAILED = 311
DEVICE_ID_MISMATCH = 312
REQUEST_ACQ_EVENTS_FAILED = 313
NONE_OF_DEVICES_ARE_ACTIVATED_FOR_DATA_ACQ = 314

# //LEVEL 4
TIMEOUT_COMMAND = 401
NOT_ABLE_TO_CLOSE_SHUTTER = 402
NOT_ABLE_TO_OPEN_SHUTTER = 403
NOT_ABLE_TO_TURN_ON_LAMP = 404
NOT_ABLE_TO_TURN_OFF_LAMP = 405

# //LEVEL 5
NO_MEMORY_ALLOCATED = 501
INVALID_MEMORY = HANDLE = 502
DEVICE_ALREADY_OPEN = 503
DEVICE_NOT_OPEN = 504
INVALID_PARAMETER_VALUE = 505
FUNCTION_NOT_AVAILABLE = 506
DEVICE_NOT_INITIALIZED = 507
FUNCTION_ABORTED = 508
FAILED_TO_LOAD_TLC_FILE = 509
LINEARIZATION_FAILED = 510
DEVICE_NOT_AVAILABLE = 511
MUX_FSM_COMMUNICATION_ERROR = 512
UNKNOWN_EEPROM_IMAGE_VERSION = 513
DZA_CONFIG_ERR = 514
ERR_GENERIC_PDETH_ERROR = 515
UNKNOWN_LS_TYPE_FOUND = 516
LIBRARY_NOT_INITIALIZED = 517

# //ERROR INFOS
INVALID_SENSORTYPE = 801
INVALID_SENSORLENGTH = 802
INVALID_FEETYPE = 803
INVALID_INTERFACETYPE = 804
INVALID_SENSORWORKMODE = 805
INVALID_CHANNEL_ID = 806
INVALID_MUX_MODE = 807
INVALID_USE_OF_FUNCTION = 808
NOT_IN_SEQ_MODUS = 809
NOT_IN_SIM_MODUS = 810
NOT_AVAILABLE_BY_MUX = 811
NO_MUX_AVAILABLE = 812
NOT_ABLE_TO_OPEN_COMPORT = 814
NOT_ABLE_TO_START_COMMUNICATION = 815
INTTIME_FOR_ACQ_ADAPTED = 816
INTTIME_FOR_DEL_ADAPTED = 817
INVALID_INTERFACE_ID = 818
FUNCTION_NOT_SUPPORTED = 819
INVALID_OS = 822
NOT_ABLE_TO_CREATE_EVENT = 823
NO_OF_IF_NOT_SUPPORTED = 824
INVALID_CONFIGURATION = 825
INVALID_E2PROM_VALUE = 826
INVALID_CHANNEL_NO = 827
READING_E2PROM_INTERFACE = 828
READING_E2PROM_FRONTEND = 829
READING_E2PROM_MUX = 830
INVALID_INDEX = 831
LOCAL_ACCESS_ONLY = 832
INVALID_SENSOR_ROWS = 833
NOT_ABLE_TO_CREATE_HANDLE = 834
NOT_ABLE_TO_CREATE_THREAD = 835
AVERAGING_VALUE_ADAPTED = 836
FIRMWARE_IS_OBSOLETE = 837
DEVICE_ARRIVAL_FAILED = 838
DEVICE_NOTIFY_NOT_AVAILABLE = 839
TOO_MANY_NOTIFY_SUBSCRIPTIONS = 840
INVALID_FLAGS = 841
INVALID_HANDLE = 842
EEPROM_IMAGE_NOT_SUPPORTED = 843
FILE_VERSION_NOT_SUPPORTED = 844
READING_BOOT_E2PROM = 845
UNKNOWN_IMAGE_VERSION = 846
INVALID_PARAMETER_SIZE = 847
LATCHMODE_NOT_SUPPORTED = 848
INVALID_NUM_NOTIFIERS = 849
NO_DEVICE_OPENED = 850
FILE_NOT_FOUND = 851
FILE_ACCESS_ERROR = 852
INVALID_TLC_FILE = 853
NO_TLC_FILE_AVAILABLE_FOR_SENSOR = 854
LINEARIZATION_PIXELNUMBER_MISMATCH = 855
NO_CHANNEL_MAPPED = 856
DZA_ERR_JUMPER_SETTINGS_ENABLED = 857
DZA_ERR_STATUS_XXX = 858
DZA_ERR_I2C_WRITE_OR_READ_FAILED = 859
DZA_ERR_COOLING = 860
MUX_FS_TIMEOUT_COMMAND = 861
LS_SECURITY_LOCK_ENGAGED = 862


# Appendix C: Typical Program Example (Fragment) for PD-PCI01V1
# // This program fragment demonstrates how to use the SDACQ32MP library functions by using two
# // PCI-boards in one PC
# // The first PCI board uses an UV sensor unit and the second PCI board uses an NIR sensor unit.
# // Calling SDACQMP_GetSpectra with parameter ‘0’ causes a common starting of two separately
# // threads for data acquisition, the function returns after the longest thread finished its acquisition
# // (depending on the integration time and average number).
# #include "sdacq32_types.h"
# #include "sdacq32mp.h"
# #include "sdacq32_error_codes.h"
# #define PCI_1 1
# #define PCI_2 2
# #define PCI_1AND2 0 // parameter for SDACQMP_GetSpectra and
# // SDACQMP_GetDarkCurrent only !
# long ret;
# LLERROR ec;
# double IntegrationTimePCI_1 = 100.0; // 100 ms
# double IntegrationTimePCI_2 = 50.0; // 50 ms
# CHANNEL_ID Channel_ID1_1 = 0; // it is important to initialize with 0
# CHANNEL_ID Channel_ID2_1 = 0; // it is important to initialize with 0
# double spectral_data_PCI_1[2048]; // pixel data for PCI board #1 (UV)
# double spectral_data_PCI_2[2048]; // pixel data for PCI board #2 (NIR)
# // initialize library
# ret = SDACQMP_InitLibrary( 0, PD_PCI01V1, 0);
# // open device driver and initialization for PCI interface card #1
# ret = SDACQMP_OpenOperationElectronicsDeviceEx( 0, PD_PCI01V1, PCI_1, 0, 0);
# // automatically configuration
# ret = SDACQMP_InitializeOperationElectronics( 0, PCI_1 );
# // open device driver and initialization for PCI interface card #2
# ret = SDACQMP_OpenOperationElectronicsDeviceEx( 0, PD_PCI01V1, PCI_2, 0, 0);
# // automatically configuration
# ret = SDACQMP_InitializeOperationElectronics( 0, PCI_2 );
# // suppress error message box if recommended
# ret = SDACQMP_ErrorMessages( FALSE );
# // allocate memory for acquisition data
# ret = SDACQMP_AllocRawData( &Channel_ID1_1 );
# ret = SDACQMP_ParaSetMapping( &Channel_ID1_1, CHANNEL_1, PCI_1 );
# ret = SDACQMP_AllocRawData( &Channel_ID2_1 );
# ret = SDACQMP_ParaSetMapping( &Channel_ID2_1, CHANNEL_1, PCI_2 );
# // change ACQ settings
# ret = SDACQMP_ParaSetIntegrationTime( &IntegrationTimePCI_1, PCI_1 ); // change integration
# time PCI #1
# ret = SDACQMP_ParaSetIntegrationTime( &IntegrationTimePCI_2, PCI_2 ); // change integration
# time PCI #2

# // do data acquisition
# ...
# ret = SDACQMP_GetDarkCurrent( PCI_1AND2 ); // do an data acquisition with both PCI cards
# if ( ret != OK )
# { // example for an error management
# SDACQMP_GetErrorCode( &ec );
#  if ( ec.l_errorlevel > 0 )
# { // execution failed
# ret = MessageBox( 0, “ GetDarkCurrent execution failed ” ,"My Message Box",
# MB_OK );
# ...
# }
# }
# else
# {
# ret = SDACQMP_GetSpectra( PCI_1AND2 ); // do an data acquisition with both PCI c
# }
# // get darkcurrent corrected data of the last acquisition for processsing
# ret = SDACQMP_GetStoredRawData( &Channel_ID1_1, spectral_data_PCI_1 ); // UV data
# ret = SDACQMP_GetStoredRawData( &Channel_ID2_1, spectral_data_PCI_2 ); // NIR data
# // do data processing
# ...
# ...
# // end program or data acquisition
# ...
# ret = SDACQMP_FreeRawData( &Channel_ID1_1 );
# ret = SDACQMP_FreeRawData( &Channel_ID2_1 );
# ret = SDACQMP_CloseOperationElectronics( PCI_1 );
# ret = SDACQMP_CloseOperationElectronics( PCI_2 );
# ...
# // finish library usage
# ret = SDACQMP_UnInitLibrary( 0 );
