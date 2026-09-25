import numpy as np

from _vendor_runtime import load_vendor_dll
from sdacq_types import *


# Load DLL
lib, dll_path = load_vendor_dll()


MAXARRAYLENGTH = 2048
NUM_PIXELS = 1024

# BINDINGS

def _bind_functions() -> None:
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


_bind_functions()


class SDACQError(RuntimeError):
    pass


def _check(ret: int, func: str) -> None:
    if ret != 0:
        raise SDACQError(f"{func} failed with error code {ret}")


# 3.1 GENERAL FUNCTIONS

def init_library(
        flags : int, 
        device_type : int, 
        res : int
        ) -> None:
    """
    Initialization of the SDACQ32MP library
    This function has to be called once before calling any other
    SDACQMP function in any application.
    """
    ret = lib.SDACQMP_InitLibrary(
        LONG(flags),
        LONG(device_type),
        LONG(res)
        )
    _check(ret, "SDACQMP_InitLibrary")


def uninit_library(
        res : int
        ) -> None:
    """
    Deintialization of the SDACQMP library.
    This function has to be called once after closing the last opened 
    operating electronics as last SDACQMP function call in any application.
    """
    ret = lib.SDACQMP_UnInitLibrary(
        LONG(res)
        )
    _check(ret, "SDACQMP_UnInitLibrary")


def open_operation_electrics_device_ex(
        init_flags : int, 
        device_type : int, 
        ID : int, 
        ipaddress : int, 
        authcode : int
        ) -> None:
    """
    Function allocates memory for a specified interface, opens the kernel
    mode device respectively initiates a connection to the device and
    links it as interface number ```ID```.
    Remarks: PD-ETH01: IP-address and device ID configuration must be done in
    advance via its web interface.
    other: set ```ipaddress``` and ```authcode``` to 0 (not used).

    Note: for init_flags
    bit0=1 suppress errors during init                                            
    bit1=1 don't close interface if function fails                                
    because of non-initialized data in EEPROMs, should be 0 otherwise;            
    bit3=1 suppress automatic configuration; other bits are reserved and must be 0
    """
    ret = lib.SDACQMP_OpenOperationElectronicsDeviceEx(
        LONG(init_flags), 
        LONG(device_type), 
        LONG(ID), 
        ULONG(ipaddress), 
        ULONG(authcode)
        )
    _check(ret, "SDACQMP_OpenOperationElectronicsDeviceEx")


def initialize_operation_electronics(
        init_flags : int, 
        ID : int
        ) -> None:
    """
    Initialization of the interface card with automatic configuration (PnP)
    These values will be reset to the related default values:
        Integration time for acquisition: 2x minimum integration time
        Integration time for deleting: 2x minimum integration time
        Average number: 1 (after first initialization)
        Hardware flash: inactive
        Ext. triggering timeout time: 60 seconds
        Shutter polarity: positive
        Reset all DOUTs

    init_flags: bit0 = 1 suppress errors during initialization.
    """
    ret = lib.SDACQMP_InitializeOperationElectronics(
        LONG(init_flags), 
        LONG(ID)
        )
    _check(ret, "SDACQMP_InitializeOperationElectronics")


def deinit_operation_electronics(
        ID : int
        ) -> None:
    """
    Deinitialization of the interface, no access is possible before new initialization.
    """
    ret = lib.SDACQMP_DeInitializeOperationElectronics(
        LONG(ID)
        )
    _check(ret, "SDACQMP_DeInitializeOperationElectronics")


def close_operation_electronics(
        ID : int
        ) -> None:
    """
    Function closes the handle of the kernel mode device and
    deallocates its memory, no access is possible before reopening the device.
    """
    ret = lib.SDACQMP_CloseOperationElectronics(
        LONG(ID)
        )
    print(ret, "SDACQMP_CloseOperationElectronics")


# 3.2 PARAMETER FUNCTIONS

def para_set_sensor_work_mode(
        workflags : int, 
        sensorworkmode : int, 
        ID : int
        ) -> None:
    """
    Initialization of the chosen interface in the new sensor work mode with
    current values.

    Parameters
    ----------
    workflags : int
      Bit 0 = 1 : suppresses errors during initialization
      Bit 1 = 1 : suppresses FIFO overflow protection
      Bit 2 = 1 : enable external trigger ready signal (DOUT3)
      Bit 4 = 1 : enable external trigger rising edge
    sensorworkmode : int, defined in sdacq_types.py
      StartNewScanWithCleaning
      StartNewScanWithoutCleaning
      SyncToContScan
      ExternalTriggerSlope
      ExternalTriggerPulse
      GetLastScan
      GetBufferedScan
      ExternalTriggerSlopeWithCleaning
      ExternalTriggerPulseWithCleaning
      [...]
    ID : int

    Returns
    -------
    None
    """
    ret = lib.SDACQMP_ParaSetSensorWorkMode(
        LONG(workflags),
        LONG(sensorworkmode),
        LONG(ID)
        )
    _check(ret, "SDACQMP_ParaSetSensorWorkMode")


def para_set_integration_time(
        integration_time : float,
        ID : int
        ) -> None:
    """
    Function sets new integration time in [ms] for the spectral data acquisition 
    of the selected interface and you will get back the new limited integration time 
    depending on the current settings, returns 'NOK' if value is limited. 
    This function should be used generally.
    """
    ret = lib.SDACQMP_ParaSetIntegrationTime(
        byref(DOUBLE(integration_time)), 
        LONG(ID),
        )
    _check(ret, "SDACQMP_ParaSetIntegrationTime")


def para_set_integration_time2(
        integration_time : int,
        ID : int,
        ) -> None:
    """
    Function sets new integration time in [ms] for the spectral data acquisition of the selected interface
    and you will get back the new limited integration time depending on the current settings,
    returns ‘NOK’ if value is limited.
    The difference to SDACQMP_ParaSetIntegrationTime() is the timer resolution
    which is 1 ms instead of 0.1 ms (Standard) so it
    is possible to use a larger integration time up to 65 seconds.
    Remarks: Not available for PD-ETH01:
    The function SDACQMP_ParaSetIntegrationTime() operates with a
    resolution of 1 µs with an enhanced range and can be used instead.
    """
    ret = lib.SDACQMP_ParaSetIntegrationTime2(
        byref(LONG(integration_time)),
        LONG(ID),
        )
    _check(ret, "SDACQMP_ParaSetIntegrationTime2")


def para_set_integration_time3(
        integration_time : int,
        ID : int,
        ) -> None:
    """
    Function sets new integration time in [ms] for the spectral data acquisition
    of the selected interface and you will get back the new limited integration time
    depending on the current settings, returns ‘NOK’ if value is limited.
    The difference to SDACQMP_ParaSetIntegrationTime()
    is the timer resolution which is 8 ms instead of 0.1 ms (Standard) so it
    is possible to use a larger integration time up to 520 seconds.
    This function is supported for PD-PCI01V1 and PD-USB01 (since
    CPLD version 2.04 and driver version 2.0.1.3) only.
    Remarks: Not available for PD-ETH01:
    The function SDACQMP_ParaSetIntegrationTime() operates with a
    resolution of 1 µs with an enhanced range and can be used instead.
    """
    ret = lib.SDACQMP_ParaSetIntegrationTime3(
        byref(LONG(integration_time)),
        LONG(ID),
        )
    _check(ret, "SDACQMP_ParaSetIntegrationTime3")


def para_set_integration_time_for_deleting(
        integration_time : float,
        ID : int,
        ) -> None:
    """
    Function sets new integration time in [ms] for sensor continuous
    readout (cleaning scans) in sensor modes which employ cleaning
    scans with a configurable integration time of the selected interface
    and you will receive the new limited integration time depending on the
    current settings, returns ‘NOK’ if value is limited or function fails.
    """
    ret = lib.SDACQMP_ParaSetIntegrationTimeForDeleting(
        byref(DOUBLE(integration_time)),
        LONG(ID),
        )
    _check(ret, "SDACQMP_ParaSetIntegrationTimeForDeleting")


def para_set_average_number(
        averages : int,
        ID : int,
        ) -> None:
    """
    Function sets new average number (1 … 100) for the spectral data
    acquisition of the selected interface and changes acquisition from
    “burst” to “averaging” mode.
    You will receive the new limited average number time depending on
    the current settings, returns ‘NOK’ if value is limited.
    """
    ret = lib.SDACQMP_ParaSetAverageNumber(
        byref(LONG(averages)),
        LONG(ID),
        )
    _check(ret, "SDACQMP_ParaSetAverageNumber")
    

def para_get_average_number_limit(
        max_average : int,
        ID : int,
        ) -> None:
    """
    Function gets maximum average number (1... 255) for the spectral
    data acquisition of the selected interface.
    """
    ret = lib.SDACQMP_ParaGetAverageNumberLimit(
        byref(LONG(max_average)),
        LONG(ID),
        )
    _check(ret, "SDACQMP_ParaGetAverageNumberLimit")


def para_set_burst_number():
    pass


def para_get_burst_number_limit():
    pass


def para_set_hardware_flash_mode2():
    pass


def para_set_flash_polarity():
    pass


def para_get_hardware_flash_mode():
    pass


def para_set_ext_trigg_timeout():
    pass


def para_set_dark_current_correction_mode():
    pass


def para_set_shutter_polarity():
    pass


def para_set_shutter_control_mode():
    pass


def para_get_integration_time_limits():
    pass


def para_get_intensity_limits():
    pass


def para_set_spec_buffer():
    pass


def para_set_roi_settings():
    pass


# 3.3 DATA ACQUISITION FUNCTIONS


def get_spectra(
        ID : int
        ) -> None:
    """
    Function reads all available channel data from the board of the chosen
    interface and stores it to the allocated and mapped memory RawSpectral data.
    If DarkCurrentCorrectionMode is enabled (default) the RawData will
    be corrected by using the last stored DarkCurrentData of the same
    channel.
    The values in the buffer are the mean values of (average) measurement in energy counts 
    covered by the pixel number.
    If the given parameter ```ID``` is '0' the function requests a data acquisition 
    of all enabled interfaces (see SDACQMP_SetInterfaceActive and
    SDACQMP_SetInterfaceInactive), otherwise only the specified interface is used.
    """
    ret = lib.SDACQMP_GetSpectra(
        LONG(ID)
        )
    _check(ret, "SDACQMP_GetSpectra")


def get_spectra_ex():
    pass


def get_dark_current(
        ID : int
        ) -> None:
    """
    Function reads all available channel data from the board of the selected interface 
    and stores it to the allocated and mapped memory as DarkCurrentData.
    The values in the buffer are the mean values of (average) measurement in energy counts 
    covered to the pixel number.

    If the given parameter ```ID``` is 0, the function requests a data acquisition 
    of all enabled interfaces (see SDACQMP_SetInterfaceActive and SDACQMP_SetInterfaceInactive), 
    otherwise only the specified interface is used

    Note: Dark current correction is enabled for all channels by default. 
    All data acquisitions following the first dark current acquisition will therefore 
    be performed with dark current correction engaged.
    """
    ret = lib.SDACQMP_GetDarkCurrent(
        LONG(ID)
        )
    _check(ret, "SDACQMP_GetDarkCurrent")


def get_dark_current_with_shutter():
    pass


def get_buffered_spectra():
    pass


def set_interface_active():
    pass


def set_interface_inactive():
    pass


# 3.4 DIGITAL I/O

def io_set_dig_output1(
        level : int,
        ID : int
        ) -> None:
    """
    Function sets the digital output #1 of the selected interface to the specified level.
    """
    ret = lib.SDACQMP_IOSetDigOutput1(
        LONG(level), 
        LONG(ID)
    )
    _check(ret, "SDACQMP_IOSetDigOutput1")



def io_set_dig_output2():
    pass


def io_set_dig_output3():
    pass


def io_set_dig_outputs():
    pass


def io_get_dig_input1():
    pass


def io_get_dig_input2():
    pass


def io_get_dig_input3():
    pass


def io_get_dig_inputs():
    pass


def para_set_input_source():
    pass


def para_set_input_latch_mode():
    pass


def get_error_code():
    pass


def get_error_code_OE():
    pass


def warning_messages_ex():
    pass


# 3.6 SPECIFIC MUX FUNCTIONS

def para_set_mux_mode():
    pass


def para_set_mux_active_channel():
    pass


# 3.7 SPECIFIC DATA STRUCTURE FUNCTIONS

def alloc_raw_data() -> int:
    """
    """
    channel_id = CHANNEL_ID(0)
    ret = lib.SDACQMP_AllocRawData(
        byref(channel_id)
        )
    _check(ret, "SDACQMP_AllocRawData")
    # print("channel_ID after alloc: ", channel_ID.value) # type: ignore
    return channel_id.value


def para_set_mapping():
    pass


def para_set_mapping(
        channel_id : int, 
        channel : int, 
        ID : int
        ) -> None:
    """
    """
    channel_id_c = CHANNEL_ID(channel_id)
    
    ret = lib.SDACQMP_ParaSetMapping(
        byref(channel_id_c), 
        LONG(channel), 
        LONG(ID)
        )
    _check(ret, "SDACQMP_ParaSetMapping")
    # print("channel_ID after mapping: ", channel_ID.value) # type: ignore


def free_raw_data(
        channel_ID : int
        ) -> None:
    """
    """
    ret = lib.SDACQMP_FreeRawData(
        byref(LONG(channel_ID))
        )
    _check(ret, "SDACQMP_FreeRawData")


# 3.8 MISC FUNCTIONS FOR ADDITIONAL COMPONENTS

# LS CONTROL

def ls_initialize():
    pass


def ls_open_shutter():
    pass


def ls_close_shutter():
    pass


def ls_power_on():
    pass


def ls_power_off():
    pass


def ls_get_shutter_position():
    pass


def ls_get_status():
    pass


def ls_get_actual_temperature():
    pass


def ls_set_temperature_alarm():
    pass


def ls_read_flash_rate():
    pass


def ls_set_flash_counter():
    pass


def ls_get_remote_status():
    pass


def ls_save_power_status():
    pass


# 3.9 DATA ACCESS FUNCTIONS

def get_stored_raw_data(
        channel_ID : int, 
        ) -> np.ndarray:
    """
    Function copies the specified Raw Data to the address range pointed
    to by 'p_data'. The allocated memory must be large enough to accommodate 
    the size of one scan. The data amount is equal to the number of pixels of 
    the sensor (sensor length, for CCD 2D operation multiplied by number of binning areas). 
    Most configurations and sensor types size do not exceed 2048 pixels.
    """
    data = (DOUBLE * MAXARRAYLENGTH)()
    ret = lib.SDACQMP_GetStoredRawData(
        byref(LONG(channel_ID)), 
        data
        )
    _check(ret, "SDACQMP_GetStoredRawData")
    return np.array(data[:NUM_PIXELS], dtype=float)


def get_stored_raw_data_burst():
    pass


def get_stored_pixel_number():
    pass


def get_stored_dark_current_data():
    pass


def delete_dark_current_data():
    pass


def get_stored_dark_mode_settings():
    pass


def get_stored_average_number():
    pass


def get_stored_burst_number():
    pass


def get_stored_integration_time():
    pass


def get_stored_timestamp():
    pass


def get_stored_intensity():
    pass


# 3.10 HARDWARE CONFIGURATION FUNCTIONS

def hwconfig__get_sensor_params_ex2():
    pass


def hwconfig_change_sensor_params_ex2():
    pass


def hwconfig_para_get_hwconfiguration_ex2():
    pass


def hwconfig_change_mux_params():
    pass


def hwconfig_get_mux_params():
    pass


# 3.11 I2C COMPONENTS

def i2c_write_1():
    pass


def i2c_read_1():
    pass


def i2c_write_N():
    pass


def i2c_read_N():
    pass


def i2c_programming():
    pass


def i2c_read_eeprom_cust_data():
    pass


def i2c_write_eeprom_cust_data():
    pass


def i2c_read_eeprom():
    pass


def i2c_write_eeprom():
    pass


def i2c_get_all_temperatures():
    pass


def i2c_get_temperature():
    pass


# 3.12 LINEARIZATION

def linearization():
    pass


def linearization_channel():
    pass


def linearization_channel_ex():
    pass
