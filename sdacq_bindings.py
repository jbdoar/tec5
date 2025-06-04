'''
Operating Electronics for Carl Zeiss MMS/MCS Spectral Sensors and Hamamatsu MOS Linear Image Sensors
SDACQ32MP 32/64 Bit Spectra Data Acquisition Library
PD-PCI01V1, PD-PCIe01V1, PD-USB01 and PD-ETH01 (Windows 7/8.1/10)
'''

from ctypes import *
from enum import Enum, IntEnum
import os

dll_path = os.path.join(os.path.dirname(__file__), 'SDACQ64MP.dll')
_lib = cdll.LoadLibrary(dll_path)

# General functions

_lib.SDACQMP_InitLibrary.argtypes = [c_long, c_long, c_long]
_lib.SDACQMP_InitLibrary.restype = c_long

_lib.SDACQMP_UnInitLibrary.argtypes = c_long
_lib.SDACQMP_UnInitLibrary.restype = c_long

_lib.SDACQMP_OpenOperationElectronicsDeviceEx.argtypes = [c_long, c_long, c_long, c_ulong, c_ulong]
_lib.SDACQMP_OpenOperationElectronicsDeviceEx.restype = c_long

_lib.SDACQMP_InitializeOperationElectronics.argtypes = [c_long, c_long]
_lib.SDACQMP_InitializeOperationElectronics.restype = c_long

_lib.SDACQMP_DeInitializeOperationElectronics.argtypes = c_long
_lib.SDACQMP_DeInitializeOperationElectronics.restype = c_long

_lib.SDACQMP_CloseOperationElectronics.argtypes = c_long
_lib.SDACQMP_CloseOperationElectronics.restype = c_long

# Parameter functions

_lib.SDACQMP_ParaSetSensorWorkMode.argtypes = [c_long, c_long, c_long]
_lib.SDACQMP_ParaSetSensorWorkMode.restype = c_long

_lib.SDACQMP_ParaSetIntegrationTime.argtypes = [POINTER(c_double), c_long]
_lib.SDACQMP_ParaSetIntegrationTime.restype = c_long

_lib.SDACQMP_ParaSetIntegrationTime2.argtypes = [POINTER(c_long), c_long]
_lib.SDACQMP_ParaSetIntegrationTime2.restype = c_long

_lib.SDACQMP_ParaSetIntegrationTime3.argtypes = [POINTER(c_long), c_long]
_lib.SDACQMP_ParaSetIntegrationTime3.restype = c_long

_lib.SDACQMP_ParaSetIntegrationTimeForDeleting.argtypes = [POINTER(c_double), c_long]
_lib.SDACQMP_ParaSetIntegrationTimeForDeleting.restype = c_long

_lib.SDACQMP_ParaSetAverageNumber.argtypes = [POINTER(c_long), c_long]
_lib.SDACQMP_ParaSetAverageNumber.restype = c_long

_lib.SDACQMP_ParaGetAverageNumberLimit.argtypes = [POINTER(c_long), c_long]
_lib.SDACQMP_ParaGetAverageNumberLimit.restype = c_long

_lib.SDACQMP_ParaSetBurstNumber.argtypes = [POINTER(c_long), c_long]
_lib.SDACQMP_ParaSetBurstNumber.restype = c_long

_lib.SDACQMP_ParaGetBurstNumberLimit.argtypes = [POINTER(c_long), c_long]
_lib.SDACQMP_ParaGetBurstNumberLimit.restype = c_long

_lib.SDACQMP_ParaSetHardwareFlashMode2.argtypes = [c_long, c_long, c_long]
_lib.SDACQMP_ParaSetHardwareFlashMode2.restype = c_long

_lib.SDACQMP_ParaSetFlashPolarity.argtypes = [c_long, c_long]
_lib.SDACQMP_ParaSetFlashPolarity.restype = c_long

_lib.SDACQMP_ParaGetHardwareFlashMode.argtypes = [POINTER(c_long), c_long]
_lib.SDACQMP_ParaGetHardwareFlashMode.restype = c_long

_lib.SDACQMP_ParaSetExtTriggTimeout.argtypes = [POINTER(c_long), c_long]
_lib.SDACQMP_ParaSetExtTriggTimeout.restype = c_long

_lib.SDACQMP_ParaSetDarkCurrentCorrectionMode.argtypes = [POINTER(CHANNEL_ID), c_long]
_lib.SDACQMP_ParaSetDarkCurrentCorrectionMode.restype = c_long

_lib.SDACQMP_ParaSetShutterPolarity.argtypes = [c_long, c_long]
_lib.SDACQMP_ParaSetShutterPolarity.restype = c_long

_lib.SDACQMP_ParaSetShutterControlMode.argtypes = [c_long, c_long]
_lib.SDACQMP_ParaSetShutterControlMode.restype = c_long

_lib.SDACQMP_ParaGetIntegrationTimeLimits.argtypes = [POINTER(c_double), POINTER(c_double), c_long]
_lib.SDACQMP_ParaGetIntegrationTimeLimits.restype = c_long

_lib.SDACQMP_ParaGetIntensityLimits.argtypes = [POINTER(c_long), POINTER(c_long), c_long]
_lib.SDACQMP_ParaGetIntensityLimits.restype = c_long

_lib.SDACQMP_ParaSetSpecBuffer.argtypes = [c_long, c_long]
_lib.SDACQMP_ParaSetSpecBuffer.restype = c_long

_lib.SDACQMP_ParaSetROISettings.argtypes = [c_long, POINTER(P_ROI_PARAMETERSET), c_long, c_long]
_lib.SDACQMP_ParaSetROISettings.restype = c_long

# Data acquisition functions

_lib.SDACQMP_GetSpectra.argtypes = c_long
_lib.SDACQMP_GetSpectra.restype = c_long

_lib.SDACQMP_GetSpectraEx.argtypes = [c_long, c_long]
_lib.SDACQMP_GetSpectraEx.restype = c_long

_lib.SDACQMP_GetDarkCurrent.argtypes = c_long
_lib.SDACQMP_GetDarkCurrent.restype = c_long

_lib.SDACQMP_GetDarkCurrentWithShutter.argtypes = [c_long, c_long]
_lib.SDACQMP_GetDarkCurrentWithShutter.restype = c_long

_lib.SDACQMP_GetBufferedSpectra.argtypes = [POINTER(c_long), POINTER(c_long), c_long]
_lib.SDACQMP_GetBufferedSpectra.restype = c_long

_lib.SDACQMP_SetInterfaceActive.argtypes = c_long
_lib.SDACQMP_SetInterfaceActive.restype = c_long

_lib.SDACQMP_SetInterfaceInActive.argtypes = c_long
_lib.SDACQMP_SetInterfaceInActive.restype = c_long

# Digital I/O

_lib.SDACQMP_IOSetDigOutput1.argtypes = [c_long, c_long]
_lib.SDACQMP_IOSetDigOutput1.restype = c_long

_lib.SDACQMP_IOSetDigOutput2.argtypes = [c_long, c_long]
_lib.SDACQMP_IOSetDigOutput2.restype = c_long

_lib.SDACQMP_IOSetDigOutput3.argtypes = [c_long, c_long]
_lib.SDACQMP_IOSetDigOutput3.restype = c_long

_lib.SDACQMP_IOSetDigOutputs.argtypes = [c_long, c_long, c_long]
_lib.SDACQMP_IOSetDigOutputs.restype = c_long

_lib.SDACQMP_IOGetDigInput1.argtypes = [POINTER(c_long), c_long]
_lib.SDACQMP_IOGetDigInput1.restype = c_long

_lib.SDACQMP_IOGetDigInput2.argtypes = [POINTER(c_long), c_long]
_lib.SDACQMP_IOGetDigInput2.restype = c_long

_lib.SDACQMP_IOGetDigInput3.argtypes = [POINTER(c_long), c_long]
_lib.SDACQMP_IOGetDigInput3.restype = c_long

_lib.SDACQMP_IOGetDigInputs.argtypes = [POINTER(c_long), c_long, c_long]
_lib.SDACQMP_IOGetDigInputs.restype = c_long

_lib.SDACQMP_ParaSetInputSource.argtypes = [c_long, c_long]
_lib.SDACQMP_ParaSetInputSource.restype = c_long

_lib.SDACQMP_ParaSetInputLatchMode.argtypes = [c_long, c_long]
_lib.SDACQMP_ParaSetInputLatchMode.restype = c_long
    
# Error information

#SDACQMP_GetErrorCode
_lib.SDACQMP_GetErrorCode.argtypes = [POINTER(P_LLERRORS)]
_lib.SDACQMP_GetErrorCode.restype = c_long

_lib.SDACQMP_WarningMessagesEx.argtypes = [c_long, c_long]
_lib.SDACQMP_WarningMessagesEx.restype = c_long

# Specific MUX functions

_lib.SDACQMP_ParaSetMUXMode.argtypes = [c_long, c_long, c_long]
_lib.SDACQMP_ParaSetMUXMode.restype = c_long

_lib.SDACQMP_ParaSetMUXActiveChannel.argtypes = [c_long, c_long]
_lib.SDACQMP_ParaSetMUXActiveChannel.restype = c_long

# Specific data structure functions

_lib.SDACQMP_AllocRawData.argtypes = POINTER(CHANNEL_ID)
_lib.SDACQMP_AllocRawData.restype = c_long

_lib.SDACQMP_ParaSetMapping.argtypes = [POINTER(CHANNEL_ID), c_long, c_long]
_lib.SDACQMP_ParaSetMapping.restype = c_long

_lib.SDACQMP_FreeRawData.argtypes = POINTER(CHANNEL_ID)
_lib.SDACQMP_FreeRawData.restype = c_long

# Misc functions for additional components

# LS control
# Note: These functions are only available if a separate LS cassette or LS flash lamp is connected to the I²C bus of the interface electronics.

_lib.SDACQMP_LS_Initialize.argtypes = [c_long, c_long, c_long, POINTER(c_long)]
_lib.SDACQMP_LS_Initialize.restype = c_long

_lib.SDACQMP_LS_OpenShutter.argtypes = [c_long, c_long, c_long]
_lib.SDACQMP_LS_OpenShutter.restype = c_long

_lib.SDACQMP_LS_CloseShutter.argtypes = [c_long, c_long, c_long]
_lib.SDACQMP_LS_CloseShutter.restype = c_long

_lib.SDACQMP_LS_PowerON.argtypes = [c_long, c_long, c_long, c_long]
_lib.SDACQMP_LS_PowerON.restype = c_long

_lib.SDACQMP_LS_PowerOFF.argtypes = [c_long, c_long, c_long, c_long]
_lib.SDACQMP_LS_PowerOFF.restype = c_long

_lib.SDACQMP_LS_GetShutterPosition.argtypes = [c_long, c_long, POINTER(c_long)]
_lib.SDACQMP_LS_GetShutterPosition.restype = c_long

_lib.SDACQMP_LS_GetStatus.argtypes = [c_long, c_long, POINTER(c_long)]
_lib.SDACQMP_LS_GetStatus.restype = c_long

_lib.SDACQMP_LS_GetActualTemperature.argtypes = [c_long, c_long, POINTER(c_long)]
_lib.SDACQMP_LS_GetActualTemperature.restype = c_long

_lib.SDACQMP_LS_SetTemperatureAlarm.argtypes = [c_long, c_long, c_long, c_long]
_lib.SDACQMP_LS_SetTemperatureAlarm.restype = c_long

_lib.SDACQMP_LS_ReadFlashRate.argtypes = [c_long, c_long, POINTER(c_long)]
_lib.SDACQMP_LS_ReadFlashRate.restype = c_long

_lib.SDACQMP_LS_SetFlashCounter.argtypes = [c_long, c_long, c_long]
_lib.SDACQMP_LS_SetFlashCounter.restype = c_long

_lib.SDACQMP_LS_GetRemoteStatus.argtypes = [c_long, c_long, POINTER(c_long)]
_lib.SDACQMP_LS_GetRemoteStatus.restype = c_long

_lib.SDACQMP_LS_SavePowerStatus.argtypes = [c_long, c_long]
_lib.SDACQMP_LS_SavePowerStatus.restype = c_long

_lib.SDACQMP_LS_GetSTRProperty.argtypes = [c_long, c_long, LS_Property, c_long, POINTER(c_char)]
_lib.SDACQMP_LS_GetSTRProperty.restype = c_long

_lib.SDACQMP_LS_GetLNGProperty.argtypes = [c_long, c_long, LS_Property, POINTER(c_long)]
_lib.SDACQMP_LS_GetLNGProperty.restype = c_long

_lib.SDACQMP_LS_SetLNGProperty.argtypes = [c_long, c_long, LS_Property, c_long]
_lib.SDACQMP_LS_SetLNGProperty.restype = c_long

_lib.SDACQMP_LS_GetDBLProperty.argtypes = [c_long, c_long, LS_Property, POINTER(c_double)]
_lib.SDACQMP_LS_GetDBLProperty.restype = c_long

_lib.SDACQMP_LS_SetDBLProperty.argtypes = [c_long, c_long, LS_Property, c_double]
_lib.SDACQMP_LS_SetDBLProperty.restype = c_long

# LS Properties
# Note:
# Properties are currently supported for the following LS types:
# - BEK-Laser
# - BEK-HMP
# Different LS types support different properties. Some of them are read-only or only
# writeable. The availability and the R/W attribute depend on LS type, firmware version
# or libraries version.

class LSProperties(Structure):
    _fields_ = [('LS_PROP_FW_VERSION', c_long),
                ('LS_PROP_FW_DATE', c_long),
                ('LS_PROP_LS_FAM', c_long),
                ('LS_PROP_LS_TYPE', c_long),
                ('LS_PROP_LS_ASSEMB', c_long),
                ('LS_PROP_SERIAL_NUMBER', c_long),
                ('LS_PROP_OP_HOURS_SEC', c_long),
                ('LS_PROP_OP_HOURS_WNG_SEC', c_long),
                ('LS_PROP_INTERLOCK_MASK', c_long),
                ('LS_PROP_INTERLOCK_NO', c_long),
                ('LS_PROP_RELEASE_INTERLOCK', c_long),
                ('LS_PROP_NOMINAL_CONDITION_OF_POWER_STATUS', c_long),
                ('LS_PROP_COM_INTERFACE', c_long),
                ('LS_PROP_OP_HOURS_MIN', c_long),
                ('LS_PROP_AVAIL_LS', c_long),
                ('LS_PROP_OP_HOURS1', c_long),
                ('LS_PROP_OP_HOURS2', c_long),
                ('LS_PROP_OP_HOURS_WNG1', c_long),
                ('LS_PROP_OP_HOURS_WNG2', c_long),
                ('LS_PROP_TEMPERATURE', c_double),
                ('LS_PROP_SHUTTER_POSITION', c_long),
                ('LS_PROP_DEFECT_LAMPS', c_long),
                ('LS_PROP_STATUS', c_long),
                ('LS_PROP_REDUNDANCY', c_long),
                ('LS_PROP_ACTIVE_LS', c_long),
                ('LS_PROP_IS_DEFECT_MESSAGE_SUPPORTED', c_long),
                ('LS_PROP_AUTOMESSAGE', c_long),
                ('LS_PROP_IS_DEFECT_MESSAGE_RECEIVED', c_long),
                ('LS_PROP_DEFECT_MESSAGE_RESULT', c_long),
                ('LS_PROP_COM_PORT', c_long),
                ('LS_TIMEOUT_SHUTTER', c_long),
                ('LS_TIMEOUT_LS1', c_long),
                ('LS_TIMEOUT_LS2', c_long),
                ('LS_PROP_ACTIVE_RED_LS', c_long),
                ('LS_PROP_LASER_CENTR_WAVE_LENGTH', c_double)
                ]


_lib.SDACQMP_HWConfig_ChangeLSParams.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long]
_lib.SDACQMP_HWConfig_ChangeLSParams.restype = c_long

_lib.SDACQMP_HWConfig_GetLSParams.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long]
_lib.SDACQMP_HWConfig_GetLSParams.restype = c_long

# Data access functions

_lib.SDACQMP_GetStoredRawData.argtypes = [CHANNEL_ID, POINTER(c_double)]
_lib.SDACQMP_GetStoredRawData.restype = c_long

_lib.SDACQMP_GetStoredRawDataBurst.argtypes = [CHANNEL_ID, c_long, POINTER(c_double)]
_lib.SDACQMP_GetStoredRawDataBurst.restype = c_long

_lib.SDACQMP_GetStoredPixelnumber.argtypes = [POINTER(CHANNEL_ID), POINTER(c_double)]
_lib.SDACQMP_GetStoredPixelnumber.restype = c_long

_lib.SDACQMP_GetStoredDarkcurrentData.argtypes = [POINTER(CHANNEL_ID), POINTER(c_double)]
_lib.SDACQMP_GetStoredDarkcurrentData.restype = c_long

_lib.SDACQMP_DeleteDarkcurrentData.argtypes = POINTER(CHANNEL_ID)
_lib.SDACQMP_DeleteDarkcurrentData.restype = c_long

_lib.SDACQMP_GetStoredDarkModeSettings.argtypes = [POINTER(CHANNEL_ID), POINTER(c_long)]
_lib.SDACQMP_GetStoredDarkModeSettings.restype = c_long

_lib.SDACQMP_GetStoredAverageNumber.argtypes = [POINTER(CHANNEL_ID), POINTER(c_long)]
_lib.SDACQMP_GetStoredAverageNumber.restype = c_long

_lib.SDACQMP_GetStoredBurstNumber.argtypes = [POINTER(CHANNEL_ID), POINTER(c_long)]
_lib.SDACQMP_GetStoredBurstNumber.restype = c_long

_lib.SDACQMP_GetStoredIntegrationtime.argtypes = [POINTER(CHANNEL_ID), POINTER(c_double)]
_lib.SDACQMP_GetStoredIntegrationtime.restype = c_long

_lib.SDACQMP_GetStoredTimeStamp.argtypes = [POINTER(CHANNEL_ID), c_long, POINTER(c_long), POINTER(_TIMEDATE_EXT), POINTER(c_longlong)]
_lib.SDACQMP_GetStoredTimeStamp.restype = c_long

_lib.SDACQMP_GetStoredIntensity.argtypes = [POINTER(CHANNEL_ID), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)] 
_lib.SDACQMP_GetStoredIntensity.restype = c_long

# Hardware configuration functions

_lib.SDACQMP_HWConfig_GetSensorParamsEx2.argtypes = [c_long, POINTER(_SENSORPARAMS_X), c_long, c_long]
_lib.SDACQMP_HWConfig_GetSensorParamsEx2.restype = c_long

_lib.SDACQMP_HWConfig_ChangeSensorParamsEx2.argtypes = [c_long, POINTER(_SENSORPARAMS_X), c_long, c_long]
_lib.SDACQMP_HWConfig_ChangeSensorParamsEx2.restype = c_long

_lib.SDACQMP_HWConfig_ParaGetHWConfigurationEx2.argtypes = [c_long, POINTER(_HWSETTINGS_X), c_long]
_lib.SDACQMP_HWConfig_ParaGetHWConfigurationEx2.restype = c_long

_lib.SDACQMP_HWConfig_ChangeMUXParams.argtypes = [c_long, c_long, c_long, c_long]
_lib.SDACQMP_HWConfig_ChangeMUXParams.restype = c_long

_lib.SDACQMP_HWConfig_GetMUXParams.argtypes = [POINTER(c_long), POINTER(c_long), POINTER(c_long), POINTER(c_long)]
_lib.SDACQMP_HWConfig_GetMUXParams.restype = c_long

# I2C components functions

_lib.SDACQMP_I2C_Write_1.argtypes = [c_long, POINTER(c_ubyte), c_long, c_long]
_lib.SDACQMP_I2C_Write_1.restype = c_long

_lib.SDACQMP_I2C_Read_1.argtypes = [c_long, POINTER(c_ubyte), c_long, c_long]
_lib.SDACQMP_I2C_Read_1.restype = c_long

_lib.SDACQMP_I2C_Write_N.argtypes = [c_long, POINTER(c_ubyte), c_long, c_long, c_long]
_lib.SDACQMP_I2C_Write_N.restype = c_long

_lib.SDACQMP_I2C_Read_N.argtypes = [c_long, POINTER(c_ubyte), c_long, c_long]
_lib.SDACQMP_I2C_Read_N.restype = c_long

_lib.SDACQMP_I2C_Programming.argtypes = [c_long, POINTER(c_ubyte), c_long, c_long, c_long]
_lib.SDACQMP_I2C_Programming.restype = c_long

_lib.SDACQMP_I2C_Read_EEPROM_CustData.argtypes = [c_long, c_long, c_long, c_long, c_long]
_lib.SDACQMP_I2C_Read_EEPROM_CustData.restype = c_long

_lib.SDACQMP_I2C_Write_EEPROM_CustData.argtypes = [c_long, c_long, POINTER(c_ubyte), c_long, c_long, c_long]
_lib.SDACQMP_I2C_Write_EEPROM_CustData.restype = c_long

_lib.SDACQMP_I2C_Read_EEPROM.argtypes = [c_long, POINTER(c_ubyte), c_long]
_lib.SDACQMP_I2C_Read_EEPROM.restype = c_long

_lib.SDACQMP_I2C_Write_EEPROM.argtypes = [c_long, POINTER(c_ubyte), c_long]
_lib.SDACQMP_I2C_Write_EEPROM.restype = c_long

_lib.SDACQMP_I2C_GetAllTemperatures.argtypes = [c_long, POINTER(_TEMPERATURE_RESULTS), c_long]
_lib.SDACQMP_I2C_GetAllTemperatures.restype = c_long

_lib.SDACQMP_I2C_GetTemperature.argtypes = [c_long, c_long, POINTER(c_float), c_long]
_lib.SDACQMP_I2C_GetTemperature.restype = c_long

# Linearization

_lib.SDACQMP_Linearization.argtypes = [c_long, c_long]
_lib.SDACQMP_Linearization.restype = c_long

_lib.SDACQMP_LinearizationChannel.argtypes = [POINTER(CHANNEL_ID), c_long, c_long] 
_lib.SDACQMP_LinearizationChannel.restype = c_long

_lib.SDACQMP_LinearizationChannelEx.argtypes = [POINTER(CHANNEL_ID), c_long, POINTER(c_wchar_p), c_long]
_lib.SDACQMP_LinearizationChannelEx.restype = c_long

######################################################################
# Appendix A: Description of the Public Data Structures / Constants sdacq32_types.h

class InterfaceTypes(Enum):
    PD_PCI01V1 = 4
    PD_USB01 = 6
    PD_ETH01 = 7
    COE_USB11 = 9
    PD_PCIE01 = 11
    SEU_CGS = 12
    DEFAULT_INTERFACECARD = PD_USB01

class ConnectorDIN(Enum):
    DIN_FEE = 0 # (Default)
    DIN_DSUB = 1
    DIN_AUX = 3 # PD_USB01 only, since PLD version 2.03

class FrontEndTypes(Enum):
    FEE_HS = 3 # FEE high speed
    FEE_HSMO = 6 # new, for Hamamatsu sensors
    FEE_1M_NMOS = 9 # Fast FEE for NMOS
    FEE_1M_NIR = 10 # Fast FEE for NIR
    FEE_1M_CCD = 11 # Fast FEE for CCD
    DEFAULT_FEETYPE = FEE_HS

class MUXTypes(Enum):
    NO_MUX = 0
    MUX_4P = 4
    MUX_8A = 5
    MUX_2OPT = 6
    MUX_FSM = 7
    MUX_O = 10
    DEFAULT_MUXTYPE = NO_MUX

class SensorTypes(Enum):
    SEN_PDA_HA_S390X = 0          # PDA NMOS Hamamatsu S390x
    SEN_CCD_HA_S7030_4 = 7        # CCD Hamamatsu S-7030-4
    SEN_CCD_HA_S7010_1 = 8        # CCD Hamamatsu S-7010-1
    SEN_CCD_HA_S9840 = 23         # CCD Hamamatsu S-9840
    SEN_CCD_HA_S11071 = 24        # CCD Hamamatsu S11071
    SEN_CCD_HA_S1115X = 25        # CCD Hamamatsu S1115x
    SEN_PDA_SU_LX_LD = 5          # PDA InGaAs SU LX / LD series
    SEN_PDA_HA_G92XX = 13         # PDA InGaAs Hamamatsu G92xx
    SEN_PDA_HA_G9212_14 = 21      # PDA InGaAs Hamamatsu G9212/14
    SEN_PDA_JU_MB = 3             # PDA InGaAs Judson MB series
    SEN_SS_CZ_MMS = 16            # Carl Zeiss MMS
    SEN_SS_CZ_MMS_UV = 1          # Carl Zeiss MMS-UV
    SEN_SS_CZ_MCS = 2             # Carl Zeiss MCS
    SEN_SS_CZ_MCS_CCD = 17        # Carl Zeiss MCS-CCD
    SEN_SS_CZ_CGS = 26            # Carl Zeiss CGS
    SEN_SS_CZ_PGS_NIR_17_SUI = 14 # Carl Zeiss PGS-NIR 1.7 512SUI
    SEN_SS_CZ_PGS_NIR_HM256 = 15  # Carl Zeiss PGS-NIR HM 256
    SEN_SS_CZ_PGS_NIR_HM512 = 28  # Carl Zeiss PGS-NIR HM 512
    SEN_SS_CZ_MMS_NIR_17 = 18     # Carl Zeiss MMS-NIR 1.7
    SEN_SS_CZ_MMS_NIR_17_HR = 19  # Carl Zeiss MMS-NIR 1.7 HR
    SEN_SS_CZ_MMS_NIR_17_JU = 20  # Carl Zeiss MMS-NIR 1.7 (Judson)
    SEN_HEAD_HA_C806X = 10        # Hamamatsu Head C806x (InGaAs)
    SEN_HEAD_HA_C7221 = 4         # Hamamatsu Head C7221 (InGaAs)
    SEN_HEAD_HA_C702X = 9         # Hamamatsu Head C702x (CCD)
    SEN_HEAD_HA_C704X = 6         # Hamamatsu Head C704x (CCD)
    SEN_HEAD_HA_C5964 = 11        # Hamamatsu Head C5964 (NMOS)
    SEN_GEN_XX_CFGFILE = 128      # Generic, defined by configuration file
    DEFAULT_SENSORTYPE = SEN_PDA_HA_S390X

class SensorLength(Enum):
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

class MuxModes(Enum):
    NOT_AVAILABLE = 0
    SEQUENTIELL = 1
    SIMULTAN = 2
    DEFAULT_MUXMODE = SEQUENTIELL

class ChannelNumbers(Enum):
    CHANNEL_1 = 1
    CHANNEL_2 = 2
    CHANNEL_3 = 3
    CHANNEL_4 = 4
    CHANNEL_5 = 5
    CHANNEL_6 = 6
    CHANNEL_7 = 7
    CHANNEL_8 = 8
    MAX_CHANNEL_NUMBER = 8

class MUX_FSM(Enum):
    # // MUX-FSM assemblies
    MUX_FSM_3CH = 1
    MUX_FSM_4CH = 2
    MUX_FSM_6CH = 3
    MUX_FSM_9CH = 4

class AverageCount(Enum):
    DEFAULT_AVERAGE = 1

class TriggerTimeout(Enum):
    DEFAULT_TIMEOUTTIME = 60000

class ShutterPolarity(Enum):
    SHUTTER_POL_POSITIV = 0
    SHUTTER_POL_NEGATIV = 1
    DEFAULT_SHUTTER_POL = SHUTTER_POL_POSITIV
    DEFAULT_CHANNEL_NUMBER = 1

class SensorWorkMode(Enum):
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

class SensorWorkModeFlags(Enum):
    SWM_SUPPRESS_ERROR_MESSAGES = 0x01
    SWM_SUPPRESS_FIFO_OVERFLOW_PROT = 0x02
    SWM_ENABLE_EXTTRIG_READY_SIGNAL = 0x04
    SWM_ENABLE_SPEC_GATE_INPUT = 0x08
    SWM_ENABLE_EXTTRIG_RISING_EDGE = 0x10
    SWM_ENABLE_ACQSTAT_SOMAA = 0x20

class _LLERROR(Structure):
    _fields_ = [("l_errorlevel", c_long),
                ("l_errorcode", c_long),
                ("str_func_name", c_char * 50),
                ("l_errorinfo", c_long),
                ("l_IF_number", c_long), # (by MOE_V1 equal to MOE_ID, not used if only one interface is used)
                ]
    
# // Global Type definitions
# typedef double *PDOUBLE; // pointer to double value
# typedef long CHANNEL_ID; // pointer to allocated data // mm / 02.10.98


class TIMEDATE_EXT(Struct):
    _fields_ = [('usec', c_ushort),
                ('msec', c_ushort),
                ('sec', c_ushort),
                ('min', c_ushort),
                ('hour', c_ushort),
                ('day', c_ushort),
                ('month', c_ushort),
                ('year', c_ushort)
                ]

class ROIParameterSet(Structure):
    _fields_ = [('lSize', c_long),
                ('lVersion', c_long), # must be zero
                ('usROI', (c_ushort * 2) * 2) # MinIndex and MaxIndex (included)
                ]

class SENSORCONFIG_X(Structure):
    _fields_ = [('sSensorType', c_short),
                ('sSensorLength', c_short),
                ('sSensorBinAreas', c_short),# CCD sensor only, default = 1
                ('sSensorPhysRows', c_short) # CCD sensor only, default = 1
                ]

class SENSORCOEFFS_X(Structure):
    _fields_ = [('dC0', c_double),
                ('dC1', c_double),
                ('dC2', c_double),
                ('dC3', c_double),
                ('dC4', c_double)]
    
class SENSORPARAMS_X(Structure):
    _fields_ = [('lSize', c_long),
                ('scfConfig', SENSORCOEFFS_X),
                ('lReserved', c_long) # for later use, must be 0
                ]
    
class HWSETTINGS_X(Structure):
    _fields_ = [('lSize', c_long),
                ('sIFType', c_short),
                ('sFEEType', c_short),
                ('sMUXType', c_short),
                ('sNumSensorChannels', c_short),
                ('lReserved', c_long),
                ('scSensor', SENSORCONFIG_X * 16)
                ]
    
class Warnings(Enum):
    WNG_DISABLE_ALL = 0x00
    WNG_ADC_OVERFLOW = 0x01 # Default: disabled
    WNG_SPEC_BUFFER_OVERFLOW = 0x02 # Default: enabled
    WNG_FIFO_OVERFLOW = 0x04
    LS_DEF_TIMEOUT_LAMPS = 80000 # 80 sec (D2)
    LS_DEF_TIMEOUT_SHUTTER = 1000 # 1 sec
    LS_HAL_ONLY = 0x01
    LS_D2_ONLY = 0x02
    LS_HAL_AND_D2 = 0x03
    LS_FLASH = 0x04
    LS_FLASH_STATE_MANUALLY = 0x00
    LS_FLASH_STATE_REMOTE = 0x01

class ShutterControlMode(Enum):
    SCM_DEFAULT_OPEN = 0x00
    SCM_DEFAULT_CLOSED = 0x01
    SCM_DEFAULT_OPEN_V1 = 0x02
    SCM_DEFAULT_MODE = SCM_DEFAULT_OPEN


######################################################################
# Appendix B: Error Codes and Additional Error Information
# sdacq32_error_codes.h
# GENERAL CONSTANTS

class ERRORTABLE(IntEnum):
    OK = 0
    NOK = -1
    WNG = -2
    # ERROR LEVELS
    HARDWARE_ERROR_FROM_DRIVER = 1
    MEMORY_ERROR = 2
    DEVICE_ERROR = 3
    FUNCTION_CALL_NOT_CORRECTLY_DONE = 4 # function partly done
    FUNCTION_CALL_IGNORED = 5 # no effect, nothing is done
    FUNCTION_CALL_EXECUTED_WITH_DEFAULT_VALUE = 6 # executed with default values ok
    FUNCTION_CALL_EXECUTED_WITH_CORRECTED_VALUE = 7 # executed with Corrected values ok
    WARNING_DACQ_CONTAINS_INVALID_PIXEL_DATA = 50 # ADC Over-/Underflow
    WARNING_SPECTRAL_DATA_LOST = 51
    # ERROR CODES
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
    # LEVEL 2
    NOT_ABLE_TO_ALLOC_MEMORY = 201
    NOT_ABLE_TO_FREE_MEMORY = 202
    NOT_ABLE_TO_LOCK_MEMORY = 203
    NOT_ABLE_TO_UNLOCK_MEMORY = 204
    NOT_ABLE_TO_REALLOC_MEMORY = 205
    NOT_ABLE_TO_RELOCK_MEMORY = 206
    # LEVEL 3
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
    # LEVEL 4
    TIMEOUT_COMMAND = 401
    NOT_ABLE_TO_CLOSE_SHUTTER = 402
    NOT_ABLE_TO_OPEN_SHUTTER = 403
    NOT_ABLE_TO_TURN_ON_LAMP = 404
    NOT_ABLE_TO_TURN_OFF_LAMP = 405
    # LEVEL 5
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
    # ERROR INFOS
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
