"""ctypes function signatures for SDACQ64MP.dll."""

from ctypes import POINTER, c_float

from .sdacq_types import *

lib = None


def bind_functions(library):
    """Attach ctypes argument and result declarations to a loaded DLL."""
    global lib
    lib = library
    _bind_all()
    return library


def _bind_all() -> None:
    """Bind argtypes and restypes"""
    _bind_general_functions()
    _bind_parameter_functions()
    _bind_data_acquisition_functions()
    _bind_digital_io()
    _bind_error_info()
    _bind_specific_mux_functions()
    _bind_specific_data_structure_functions()
    _bind_misc_functions()
    _bind_data_access_functions()
    _bind_hardware_config_functions()
    _bind_i2c_functions()
    _bind_linearization_functions()


def _bind_general_functions():
    # SDACQMP_InitLibrary
    lib.SDACQMP_InitLibrary.argtypes = [
        LONG, 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_InitLibrary.restype = LONG

    # SDACQMP_UnInitLibrary
    lib.SDACQMP_UnInitLibrary.argtypes = [
        LONG,
        ]
    lib.SDACQMP_UnInitLibrary.restype = LONG

    # SDACQMP_OpenOperationElectronicsDeviceEx
    lib.SDACQMP_OpenOperationElectronicsDeviceEx.argtypes = [
        LONG, 
        LONG, 
        LONG, 
        ULONG, 
        ULONG,
        ]
    lib.SDACQMP_OpenOperationElectronicsDeviceEx.restype = LONG

    # SDACQMP_InitializeOperationElectronics
    lib.SDACQMP_InitializeOperationElectronics.argtypes = [
        LONG, 
        LONG,
        ]
    lib.SDACQMP_InitializeOperationElectronics.restype = LONG

    # SDACQMP_DeInitializeOperationElectronics
    lib.SDACQMP_DeInitializeOperationElectronics.argtypes = [
        LONG,
        ]
    lib.SDACQMP_DeInitializeOperationElectronics.restype = LONG

    # SDACQMP_CloseOperationElectronics
    lib.SDACQMP_CloseOperationElectronics.argtypes = [
        LONG,
        ]
    lib.SDACQMP_CloseOperationElectronics.restype = LONG


def _bind_parameter_functions():
    # SDACQMP_ParaSetSensorWorkMode
    lib.SDACQMP_ParaSetSensorWorkMode.argtypes = [
        LONG, 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_ParaSetSensorWorkMode.restype = LONG

    # SDACQMP_ParaSetIntegrationTime (Standard)
    lib.SDACQMP_ParaSetIntegrationTime.argtypes = [
        POINTER(DOUBLE), 
        LONG,
        ]
    lib.SDACQMP_ParaSetIntegrationTime.restype = LONG

    # SDACQMP_ParaSetIntegrationTime2
    lib.SDACQMP_ParaSetIntegrationTime2.argtypes = [
        POINTER(LONG), 
        LONG,
        ]
    lib.SDACQMP_ParaSetIntegrationTime2.restype = LONG

    # SDACQMP_ParaSetIntegrationTime3
    lib.SDACQMP_ParaSetIntegrationTime3.argtypes = [
        POINTER(LONG), 
        LONG,
        ]
    lib.SDACQMP_ParaSetIntegrationTime3.restype = LONG

    # SDACQMP_ParaSetIntegrationTimeForDeleting
    lib.SDACQMP_ParaSetIntegrationTimeForDeleting.argtypes = [
        POINTER(DOUBLE), 
        LONG,
        ]
    lib.SDACQMP_ParaSetIntegrationTimeForDeleting.restype = LONG

    # SDACQMP_ParaSetAverageNumber
    lib.SDACQMP_ParaSetAverageNumber.argtypes = [
        POINTER(LONG), 
        LONG,
        ]
    lib.SDACQMP_ParaSetAverageNumber.restype = LONG
    
    # SDACQMP_ParaGetAverageNumberLimit
    lib.SDACQMP_ParaGetAverageNumberLimit.argtypes = [
        POINTER(LONG), 
        LONG,
        ]
    lib.SDACQMP_ParaGetAverageNumberLimit.restype = LONG

    # SDACQMP_ParaSetBurstNumber
    lib.SDACQMP_ParaSetBurstNumber.argtypes = [
        POINTER(LONG), 
        LONG,
        ]
    lib.SDACQMP_ParaSetBurstNumber.restype = LONG

    # SDACQMP_ParaGetBurstNumberLimit
    lib.SDACQMP_ParaGetBurstNumberLimit.argtypes = [
        POINTER(LONG), 
        LONG,
        ]
    lib.SDACQMP_ParaGetBurstNumberLimit.restype = LONG

    # SDACQMP_ParaSetHardwareFlashMode2
    lib.SDACQMP_ParaSetHardwareFlashMode2.argtypes = [
        LONG, 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_ParaSetHardwareFlashMode2.restype = LONG
 
    # SDACQMP_ParaSetFlashPolarity
    lib.SDACQMP_ParaSetFlashPolarity.argtypes = [
        LONG, 
        LONG,
        ]
    lib.SDACQMP_ParaSetFlashPolarity.restype = LONG

    # SDACQMP_ParaGetHardwareFlashMode
    lib.SDACQMP_ParaGetHardwareFlashMode.argtypes = [
        POINTER(LONG), 
        LONG,
        ]
    lib.SDACQMP_ParaGetHardwareFlashMode.restype = LONG
    
    # SDACQMP_ParaSetExtTriggTimeout
    lib.SDACQMP_ParaSetExtTriggTimeout.argtypes = [
        POINTER(LONG), 
        LONG,
        ]
    lib.SDACQMP_ParaSetExtTriggTimeout.restype = LONG
    
    # SDACQMP_ParaSetDarkCurrentCorrectionMode
    lib.SDACQMP_ParaSetDarkCurrentCorrectionMode.argtypes = [
        POINTER(CHANNEL_ID), 
        LONG,
        ]
    lib.SDACQMP_ParaSetDarkCurrentCorrectionMode.restype = LONG
    
    # SDACQMP_ParaSetShutterPolarity
    lib.SDACQMP_ParaSetShutterPolarity.argtypes = [
        LONG, 
        LONG,
        ]
    lib.SDACQMP_ParaSetShutterPolarity.restype = LONG
    
    # SDACQMP_ParaSetShutterControlMode
    lib.SDACQMP_ParaSetShutterControlMode.argtypes = [
        LONG, 
        LONG,
        ]
    lib.SDACQMP_ParaSetShutterControlMode.restype = LONG
    
    # SDACQMP_ParaGetIntegrationTimeLimits
    lib.SDACQMP_ParaGetIntegrationTimeLimits.argtypes = [
        POINTER(DOUBLE), 
        POINTER(DOUBLE), 
        LONG,
        ]
    lib.SDACQMP_ParaGetIntegrationTimeLimits.restype = LONG
    
    # SDACQMP_ParaGetIntensityLimits
    lib.SDACQMP_ParaGetIntensityLimits.argtypes = [
        POINTER(LONG), 
        POINTER(LONG), 
        LONG,
        ]
    lib.SDACQMP_ParaGetIntensityLimits.restype = LONG
    
    # SDACQMP_ParaSetSpecBuffer
    lib.SDACQMP_ParaSetSpecBuffer.argtypes = [
        LONG, 
        LONG,
        ]
    lib.SDACQMP_ParaSetSpecBuffer.restype = LONG
    
    # SDACQMP_ParaSetROISettings
    lib.SDACQMP_ParaSetROISettings.argtypes = [
        LONG, 
        POINTER(ROI_PARAMETERSET), 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_ParaSetROISettings.restype = LONG


def _bind_data_acquisition_functions():
    # SDACQMP_GetSpectra
    lib.SDACQMP_GetSpectra.argtypes = [
        LONG,
        ]
    lib.SDACQMP_GetSpectra.restype = LONG

    # SDACQMP_GetSpectraEx
    lib.SDACQMP_GetSpectraEx.argtypes = [
        LONG, 
        LONG,
        ]
    lib.SDACQMP_GetSpectraEx.restype = LONG

    # SDACQMP_GetDarkCurrent
    lib.SDACQMP_GetDarkCurrent.argtypes = [
        LONG,
        ]
    lib.SDACQMP_GetDarkCurrent.restype = LONG

    # SDACQMP_GetDarkCurrentWithShutter
    lib.SDACQMP_GetDarkCurrentWithShutter.argtypes = [
        LONG, 
        LONG,
        ]
    lib.SDACQMP_GetDarkCurrentWithShutter.restype = LONG

    # SDACQMP_GetBufferedSpectra
    lib.SDACQMP_GetBufferedSpectra.argtypes = [
        POINTER(LONG), 
        POINTER(LONG), 
        LONG,
        ]
    lib.SDACQMP_GetBufferedSpectra.restype = LONG

    # SDACQMP_SetInterfaceActive
    lib.SDACQMP_SetInterfaceActive.argtypes = [
        LONG,
        ]
    lib.SDACQMP_SetInterfaceActive.restype = LONG

    # SDACQMP_SetInterfaceInActive
    lib.SDACQMP_SetInterfaceInActive.argtypes = [
        LONG,
        ]
    lib.SDACQMP_SetInterfaceInActive.restype = LONG


def _bind_digital_io():
    # SDACQMP_IOSetDigOutput1
    lib.SDACQMP_IOSetDigOutput1.argtypes = [
        LONG, 
        LONG,
        ]
    lib.SDACQMP_IOSetDigOutput1.restype = LONG

    # SDACQMP_IOSetDigOutput2
    lib.SDACQMP_IOSetDigOutput2.argtypes = [
        LONG, 
        LONG,
        ]
    lib.SDACQMP_IOSetDigOutput2.restype = LONG

    # SDACQMP_IOSetDigOutput3
    lib.SDACQMP_IOSetDigOutput3.argtypes = [
        LONG, 
        LONG,
        ]
    lib.SDACQMP_IOSetDigOutput3.restype = LONG

    # SDACQMP_IOSetDigOutputs
    lib.SDACQMP_IOSetDigOutputs.argtypes = [
        LONG, 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_IOSetDigOutputs.restype = LONG

    # SDACQMP_IOGetDigInput1
    lib.SDACQMP_IOGetDigInput1.argtypes = [
        POINTER(LONG), 
        LONG,
        ]
    lib.SDACQMP_IOGetDigInput1.restype = LONG

    # SDACQMP_IOGetDigInput2
    lib.SDACQMP_IOGetDigInput2.argtypes = [
        POINTER(LONG), 
        LONG,
        ]
    lib.SDACQMP_IOGetDigInput2.restype = LONG

    # SDACQMP_IOGetDigInput3
    lib.SDACQMP_IOGetDigInput3.argtypes = [
        POINTER(LONG), 
        LONG,
        ]
    lib.SDACQMP_IOGetDigInput3.restype = LONG

    # SDACQMP_IOGetDigInputs
    lib.SDACQMP_IOGetDigInputs.argtypes = [
        POINTER(LONG), 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_IOGetDigInputs.restype = LONG

    # SDACQMP_ParaSetInputSource
    lib.SDACQMP_ParaSetInputSource.argtypes = [
        LONG, 
        LONG,
        ]
    lib.SDACQMP_ParaSetInputSource.restype = LONG

    # SDACQMP_ParaSetInputLatchMode
    lib.SDACQMP_ParaSetInputLatchMode.argtypes = [
        LONG, 
        LONG,
        ]
    lib.SDACQMP_ParaSetInputLatchMode.restype = LONG


def _bind_error_info():
    # SDACQMP_GetErrorCode
    lib.SDACQMP_GetErrorCode.argtypes = [
        POINTER(LLERROR),
        ]
    lib.SDACQMP_GetErrorCode.restype = LONG

    # SDACQMP_GetErrorCodeOE
    lib.SDACQMP_GetErrorCodeOE.argtypes = [
        POINTER(LLERROR),
        ]
    lib.SDACQMP_GetErrorCodeOE.restype = LONG

    # SDACQMP_WarningMessagesEx
    lib.SDACQMP_WarningMessagesEx.argtypes = [
        LONG, 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_WarningMessagesEx.restype = LONG


def _bind_specific_mux_functions():
    # SDACQMP_ParaSetMUXMode
    lib.SDACQMP_ParaSetMUXMode.argtypes = [
        LONG, 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_ParaSetMUXMode.restype = LONG

    # SDACQMP_ParaSetMUXActiveChannel
    lib.SDACQMP_ParaSetMUXActiveChannel.argtypes = [
        LONG, 
        LONG,
        ]
    lib.SDACQMP_ParaSetMUXActiveChannel.restype = LONG


def _bind_specific_data_structure_functions():
    # SDACQMP_AllocRawData
    lib.SDACQMP_AllocRawData.argtypes = [
        POINTER(CHANNEL_ID),
        ]
    lib.SDACQMP_AllocRawData.restype = LONG

    # SDACQMP_ParaSetMapping
    lib.SDACQMP_ParaSetMapping.argtypes = [
        POINTER(CHANNEL_ID), 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_ParaSetMapping.restype = LONG

    # SDACQMP_FreeRawData
    lib.SDACQMP_FreeRawData.argtypes = [
        POINTER(CHANNEL_ID),
        ]
    lib.SDACQMP_FreeRawData.restype = LONG


def _bind_misc_functions():
    # SDACQMP_LS_Initialize
    lib.SDACQMP_LS_Initialize.argtypes = [
        LONG, 
        LONG, 
        LONG, 
        POINTER(LONG),
        ]
    lib.SDACQMP_LS_Initialize.restype = LONG

    # SDACQMP_LS_OpenShutter
    lib.SDACQMP_LS_OpenShutter.argtypes = [
        LONG, 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_LS_OpenShutter.restype = LONG

    # SDACQMP_LS_CloseShutter
    lib.SDACQMP_LS_CloseShutter.argtypes = [
        LONG, 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_LS_CloseShutter.restype = LONG

    # SDACQMP_LS_PowerON
    lib.SDACQMP_LS_PowerON.argtypes = [
        LONG, 
        LONG, 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_LS_PowerON.restype = LONG

    # SDACQMP_LS_PowerOFF
    lib.SDACQMP_LS_PowerOFF.argtypes = [
        LONG, 
        LONG, 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_LS_PowerOFF.restype = LONG

    # SDACQMP_LS_GetShutterPosition
    lib.SDACQMP_LS_GetShutterPosition.argtypes = [
        LONG, 
        LONG, 
        POINTER(LONG),
        ]
    lib.SDACQMP_LS_GetShutterPosition.restype = LONG

    # SDACQMP_LS_GetStatus
    lib.SDACQMP_LS_GetStatus.argtypes = [
        LONG, 
        LONG, 
        POINTER(LONG),
        ]
    lib.SDACQMP_LS_GetStatus.restype = LONG

    # SDACQMP_LS_GetActualTemperature
    lib.SDACQMP_LS_GetActualTemperature.argtypes = [
        LONG, 
        LONG, 
        POINTER(LONG),
        ]
    lib.SDACQMP_LS_GetActualTemperature.restype = LONG

    # SDACQMP_LS_SetTemperatureAlarm
    lib.SDACQMP_LS_SetTemperatureAlarm.argtypes = [
        LONG, 
        LONG, 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_LS_SetTemperatureAlarm.restype = LONG

    # SDACQMP_LS_ReadFlashRate
    lib.SDACQMP_LS_ReadFlashRate.argtypes = [
        LONG, 
        LONG, 
        POINTER(LONG),
        ]
    lib.SDACQMP_LS_ReadFlashRate.restype = LONG

    # SDACQMP_LS_SetFlashCounter
    lib.SDACQMP_LS_SetFlashCounter.argtypes = [
        LONG, 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_LS_SetFlashCounter.restype = LONG

    # SDACQMP_LS_GetRemoteStatus
    lib.SDACQMP_LS_GetRemoteStatus.argtypes = [
        LONG, 
        LONG, 
        POINTER(LONG),
        ]
    lib.SDACQMP_LS_GetRemoteStatus.restype = LONG

    # SDACQMP_LS_SavePowerStatus
    lib.SDACQMP_LS_SavePowerStatus.argtypes = [
        LONG, 
        LONG,
        ]
    lib.SDACQMP_LS_SavePowerStatus.restype = LONG

    # Property access and LS hardware configuration. These declarations are
    # retained from the vendor API transcription; they still need comparison
    # against a matching sdacq32.h release.
    lib.SDACQMP_LS_GetSTRProperty.argtypes = [
        LONG, LONG, LONG, LONG, POINTER(CHAR),
        ]
    lib.SDACQMP_LS_GetSTRProperty.restype = LONG

    lib.SDACQMP_LS_GetLNGProperty.argtypes = [
        LONG, LONG, LONG, POINTER(LONG),
        ]
    lib.SDACQMP_LS_GetLNGProperty.restype = LONG

    lib.SDACQMP_LS_SetLNGProperty.argtypes = [
        LONG, LONG, LONG, LONG,
        ]
    lib.SDACQMP_LS_SetLNGProperty.restype = LONG

    lib.SDACQMP_LS_GetDBLProperty.argtypes = [
        LONG, LONG, LONG, POINTER(DOUBLE),
        ]
    lib.SDACQMP_LS_GetDBLProperty.restype = LONG

    lib.SDACQMP_LS_SetDBLProperty.argtypes = [
        LONG, LONG, LONG, DOUBLE,
        ]
    lib.SDACQMP_LS_SetDBLProperty.restype = LONG

    lib.SDACQMP_HWConfig_ChangeLSParams.argtypes = [
        LONG, LONG, LONG, LONG, LONG, LONG,
        ]
    lib.SDACQMP_HWConfig_ChangeLSParams.restype = LONG

    lib.SDACQMP_HWConfig_GetLSParams.argtypes = [
        LONG, LONG, LONG, LONG, LONG, LONG,
        ]
    lib.SDACQMP_HWConfig_GetLSParams.restype = LONG


def _bind_data_access_functions():
    # SDACQMP_GetStoredRawData
    lib.SDACQMP_GetStoredRawData.argtypes = [
        POINTER(CHANNEL_ID), 
        POINTER(DOUBLE),
        ]
    lib.SDACQMP_GetStoredRawData.restype = LONG

    # SDACQMP_GetStoredRawDataBurst
    lib.SDACQMP_GetStoredRawDataBurst.argtypes = [
        POINTER(CHANNEL_ID), 
        LONG, 
        POINTER(DOUBLE),
        ]
    lib.SDACQMP_GetStoredRawDataBurst.restype = LONG

    # SDACQMP_GetStoredPixelnumber
    lib.SDACQMP_GetStoredPixelnumber.argtypes = [
        POINTER(CHANNEL_ID), 
        POINTER(DOUBLE),
        ]
    lib.SDACQMP_GetStoredPixelnumber.restype = LONG

    # SDACQMP_GetStoredDarkcurrentData
    lib.SDACQMP_GetStoredDarkcurrentData.argtypes = [
        POINTER(CHANNEL_ID), 
        POINTER(DOUBLE),
        ]
    lib.SDACQMP_GetStoredDarkcurrentData.restype = LONG

    # SDACQMP_DeleteDarkcurrentData
    lib.SDACQMP_DeleteDarkcurrentData.argtypes = [
        POINTER(CHANNEL_ID),
        ]
    lib.SDACQMP_DeleteDarkcurrentData.restype = LONG

    # SDACQMP_GetStoredDarkModeSettings
    lib.SDACQMP_GetStoredDarkModeSettings.argtypes = [
        POINTER(CHANNEL_ID), 
        POINTER(LONG),
        ]
    lib.SDACQMP_GetStoredDarkModeSettings.restype = LONG

    # SDACQMP_GetStoredAverageNumber
    lib.SDACQMP_GetStoredAverageNumber.argtypes = [
        POINTER(CHANNEL_ID), 
        POINTER(LONG),
        ]
    lib.SDACQMP_GetStoredAverageNumber.restype = LONG

    # SDACQMP_GetStoredBurstNumber
    lib.SDACQMP_GetStoredBurstNumber.argtypes = [
        POINTER(CHANNEL_ID), 
        POINTER(LONG),
        ]
    lib.SDACQMP_GetStoredBurstNumber.restype = LONG

    # SDACQMP_GetStoredIntegrationtime
    lib.SDACQMP_GetStoredIntegrationtime.argtypes = [
        POINTER(CHANNEL_ID), 
        POINTER(DOUBLE),
        ]
    lib.SDACQMP_GetStoredIntegrationtime.restype = LONG

    # SDACQMP_GetStoredTimeStamp
    lib.SDACQMP_GetStoredTimeStamp.argtypes = [
        POINTER(CHANNEL_ID), 
        LONG, 
        POINTER(LONG), 
        POINTER(TIMEDATE_EXT), 
        POINTER(LONGLONG),
        ]
    lib.SDACQMP_GetStoredTimeStamp.restype = LONG

    # SDACQMP_GetStoredIntensity
    lib.SDACQMP_GetStoredIntensity.argtypes = [
        POINTER(CHANNEL_ID), 
        POINTER(DOUBLE), 
        POINTER(DOUBLE), 
        POINTER(DOUBLE), 
        POINTER(DOUBLE),
        ]
    lib.SDACQMP_GetStoredIntensity.restype = LONG


def _bind_hardware_config_functions():
    # SDACQMP_HWConfig_GetSensorParamsEx2
    lib.SDACQMP_HWConfig_GetSensorParamsEx2.argtypes = [
        LONG, 
        POINTER(SENSORPARAMS_X), 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_HWConfig_GetSensorParamsEx2.restype = LONG

    # SDACQMP_HWConfig_ChangeSensorParamsEx2
    lib.SDACQMP_HWConfig_ChangeSensorParamsEx2.argtypes = [
        LONG, 
        POINTER(SENSORPARAMS_X), 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_HWConfig_ChangeSensorParamsEx2.restype = LONG

    # SDACQMP_HWConfig_ParaGetHWConfigurationEx2
    lib.SDACQMP_HWConfig_ParaGetHWConfigurationEx2.argtypes = [
        LONG, 
        POINTER(HWSETTINGS_X), 
        LONG,
        ]
    lib.SDACQMP_HWConfig_ParaGetHWConfigurationEx2.restype = LONG

    # SDACQMP_HWConfig_ChangeMUXParams
    lib.SDACQMP_HWConfig_ChangeMUXParams.argtypes = [
        LONG, 
        LONG, 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_HWConfig_ChangeMUXParams.restype = LONG

    # SDACQMP_HWConfig_GetMUXParams
    lib.SDACQMP_HWConfig_GetMUXParams.argtypes = [
        POINTER(LONG), 
        POINTER(LONG), 
        POINTER(LONG), 
        POINTER(LONG),
        ]
    lib.SDACQMP_HWConfig_GetMUXParams.restype = LONG


def _bind_i2c_functions():
    # SDACQMP_I2C_Write_1
    lib.SDACQMP_I2C_Write_1.argtypes = [
        LONG, 
        POINTER(UCHAR), 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_I2C_Write_1.restype = LONG

    # SDACQMP_I2C_Read_1
    lib.SDACQMP_I2C_Read_1.argtypes = [
        LONG, 
        POINTER(UCHAR), 
        LONG, 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_I2C_Read_1.restype = LONG

    # SDACQMP_I2C_Write_N
    lib.SDACQMP_I2C_Write_N.argtypes = [
        LONG, 
        POINTER(UCHAR), 
        LONG, 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_I2C_Write_N.restype = LONG

    # SDACQMP_I2C_Read_N
    lib.SDACQMP_I2C_Read_N.argtypes = [
        LONG, 
        POINTER(UCHAR), 
        LONG, 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_I2C_Read_N.restype = LONG

    # SDACQMP_I2C_Programming
    lib.SDACQMP_I2C_Programming.argtypes = [
        LONG, 
        POINTER(UCHAR), 
        LONG, 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_I2C_Programming.restype = LONG

    # SDACQMP_I2C_Read_EEPROM_CustData
    lib.SDACQMP_I2C_Read_EEPROM_CustData.argtypes = [
        LONG, 
        LONG, 
        POINTER(UCHAR), 
        LONG, 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_I2C_Read_EEPROM_CustData.restype = LONG

    # SDACQMP_I2C_Write_EEPROM_CustData
    lib.SDACQMP_I2C_Write_EEPROM_CustData.argtypes = [
        LONG, 
        LONG, 
        POINTER(UCHAR), 
        LONG, 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_I2C_Write_EEPROM_CustData.restype = LONG

    # SDACQMP_I2C_Read_EEPROM
    lib.SDACQMP_I2C_Read_EEPROM.argtypes = [
        LONG, 
        POINTER(UCHAR), 
        LONG,
        ]
    lib.SDACQMP_I2C_Read_EEPROM.restype = LONG

    # SDACQMP_I2C_Write_EEPROM
    lib.SDACQMP_I2C_Write_EEPROM.argtypes = [
        LONG, 
        POINTER(UCHAR), 
        LONG,
        ]
    lib.SDACQMP_I2C_Write_EEPROM.restype = LONG

    # SDACQMP_I2C_GetAllTemperatures
    lib.SDACQMP_I2C_GetAllTemperatures.argtypes = [
        LONG, 
        POINTER(TEMPERATURE_RESULTS), 
        LONG,
        ]
    lib.SDACQMP_I2C_GetAllTemperatures.restype = LONG

    # SDACQMP_I2C_GetTemperature
    lib.SDACQMP_I2C_GetTemperature.argtypes = [
        LONG, 
        LONG, 
        POINTER(c_float), 
        LONG,
        ]
    lib.SDACQMP_I2C_GetTemperature.restype = LONG


def _bind_linearization_functions():
    # SDACQMP_Linearization
    lib.SDACQMP_Linearization.argtypes = [
        LONG, 
        LONG,
        ]
    lib.SDACQMP_Linearization.restype = LONG


    # SDACQMP_LinearizationChannel
    lib.SDACQMP_LinearizationChannel.argtypes = [
        POINTER(CHANNEL_ID), 
        LONG, 
        LONG,
        ]
    lib.SDACQMP_LinearizationChannel.restype = LONG


    # SDACQMP_LinearizationChannelEx
    lib.SDACQMP_LinearizationChannelEx.argtypes = [
        POINTER(CHANNEL_ID), 
        LONG, 
        PTCHAR, 
        LONG,
        ]
    lib.SDACQMP_LinearizationChannelEx.restype = LONG


