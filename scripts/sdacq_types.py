from ctypes import *

# INTERFACE type
PD_PCI01V1 = 4
PD_USB01 = 6
PD_ETH01 = 7
COE_USB11 = 9
PD_PCIE01 = 11
SEU_CGS	= 12
CME_USB	= 13
CFE_USB	= 14

DEFAULT_INTERFACECARD = PD_USB01


# CONNECTOR for digital input, SDACQMP_ParaSetInputSource()
DIN_FEE = 0 # PD_PCI01C1, PD_10401V1, PD_USB01 (DEFAULT)
DIN_DSUB = 1 # PD_PCI01V1, PD_10401V1, PD-USB01
DIN_AUX = 3 # PD_USB01 only


# FRONTEND type
FEE_HS = 3 # FEE high speed
FEE_HSMO = 6 # for Hamamatsu detector heads
FEE_1M_NMOS = 9 # Fast FEE for NMOS
FEE_1M_NIR = 10 # Fast FEE for NIR
FEE_1M_CCD = 11	# Fast FEE for CCD
FEE_1M_CMOS = 14 # Fast FEE for CMOS

DEFAULT_FEETYPE = FEE_HS


# MUX type
NO_MUX = 0
MUX_4P = 4
MUX_8A = 5
MUX_2OPT = 6
MUX_FSM = 7
MUX_FS = MUX_FSM	
MUX_O = 10
MUX_BUILT_IN = 11
MUX_FS_LEONI = 12
MUX_FS_HELLMA = 13
DEFAULT_MUXTYPE = NO_MUX


# SENSOR type
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
SEN_PDA_HA_S12198 = 30 # PDA CMOS Hamamatsu S12198
SEN_PDA_HA_S11637 = 31 # PDA CMOS Hamamatsu S11637
SEN_PDA_HA_S11639 = 32 # PDA CMOS Hamamatsu S11639
SEN_PDA_HA_S13496 = 33 # PDA CMOS Hamamatsu S13496
SEN_PDA_HA_S11639_AB = 34 # PDA CMOS Hamamatsu S11639 AB
SEN_PDA_HA_S13496_AB = 35 # PDA CMOS Hamamatsu S13496 AB

SEN_SS_CZ_MMS = 16 # Carl Zeiss MMS
SEN_SS_CZ_MMS_UV = 1 # Carl Zeiss MMS-UV
SEN_SS_CZ_MCS = 2 # Carl Zeiss MCS
SEN_SS_CZ_MCS_CCD = 17 # Carl Zeiss MCS-CCD
SEN_SS_CZ_CGS = 26 # Carl Zeiss CGS
SEN_SS_CZ_PGS_NIR_17_SUI = 14 # Carl Zeiss PGS-NIR 1.7 512SUI
SEN_SS_CZ_PGS_NIR_HM256	= 15 # Carl Zeiss PGS-NIR HM 256
SEN_SS_CZ_PGS_NIR_22_HPK = SEN_SS_CZ_PGS_NIR_HM256
SEN_SS_CZ_PGS_NIR_HM512	= 28 # Carl Zeiss PGS-NIR HM 512
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


# SENSOR length
PX128 = 128
PX256 = 256
PX512 = 512
PX532 = 532
PX1024 = 1024
PX1044 = 1044
PX2048 = 2048
PX2068 = 2068
PX2080 = 2080
PX4096 = 4096
PX8X532 = 4256
PX8X1044 = 8352
DEFAULT_SENSORLENGTH = PX256


# SENSOR ROWS
DEFAULT_SENSORROWS = 1


# MUX mode
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

MAX_CHANNEL_NUMBER_EL = 8
MAX_CHANNEL_NUMBER_FSM = 16
MAX_CHANNEL_NUMBER_FS_LEONI = 32
MAX_CHANNEL_NUMBER = MAX_CHANNEL_NUMBER_EL


# MUX-FSM assemblies
MUX_FSM_3CH = 1
MUX_FSM_4CH = 2
MUX_FSM_6CH = 3
MUX_FSM_9CH = 4
MUX_FSM_16CH = 6
MUX_FS_LEONI_32CH = 11
MUX_FS_HELLMA_10CH = 12
MUX_FS_HELLMA_16CH = 13


# Average count
DEFAULT_AVERAGE = 1


# ext. trigger Timeouttime
DEFAULT_TIMEOUTTIME = 60000 # 60s


# Shutter polarity
SHUTTER_POL_POSITIV = 0
SHUTTER_POL_NEGATIV = 1
DEFAULT_SHUTTER_POL = SHUTTER_POL_POSITIV
DEFAULT_CHANNEL_NUMBER = 1


# sensor work modes
StartNewScanWithCleaning = 0x0001
StartNewScanWithoutCleaning = 0x0002
SyncToContScan = 0x0003
ExternalTriggerSlope = 0x0004
ExternalTriggerPulse = 0x0005
GetLastScan = 0x0006
GetBufferedScan = 0x0007
ExternalTriggerSlopeWithCleaning = 0x0008
ExternalTriggerPulseWithCleaning = 0x0009
ExternalTriggerScanSlope = 0x000A
ExternalTriggerScanPulse = 0x000B
ExternalTriggerCycleSlope_WithCleaningSync = 0x000C
ExternalTriggerCyclePulse_WithCleaningSync = 0x000D

ExternalTriggerScanSlope_Buffered = 0x0030
ExternalTriggerScanPulse_Buffered = 0x0031
ExternalTriggerCycleSlope_Buffered = 0x0032
ExternalTriggerCyclePulse_Buffered = 0x0033

DEFAULT_SENSOR_WORK_MODE = SyncToContScan


SWM_SUPPRESS_ERROR_MESSAGES = 0x01
SWM_SUPPRESS_FIFO_OVERFLOW_PROT = 0x02
SWM_ENABLE_EXTTRIG_READY_SIGNAL = 0x04
SWM_ENABLE_SPEC_GATE_INPUT = 0x08
SWM_ENABLE_EXTTRIG_RISING_EDGE = 0x10
SWM_ENABLE_ACQSTAT_SOMAA = 0x20
SWM_ENABLE_DIN_STATUS_PIXEL = 0x40
SWM_ENABLE_BUCKETCOUNTER = 0x80
SWM_ENABLE_DUAL_INTTIME = 0x100


# TYPEDEFS
DOUBLE = c_double
CHAR = c_char
FLOAT = c_float
LONG = c_long
LONGLONG = c_longlong
PTCHAR = c_wchar_p
SHORT = c_short
UCHAR = c_ubyte
ULONG = c_ulong
USHORT = c_ushort

PDOUBLE = POINTER(DOUBLE)
CHANNEL_ID = LONG
# channel_ID = CHANNEL_ID(0)

# STRUCTS

class LLERROR(Structure):
    # LL means low level
    _fields_ = [
        ('l_errorlevel', LONG), # error level
        ('l_errorcode', LONG), # error code
        ('str_func_name', CHAR * 50), # function name
        ('l_errorinfo', LONG), # additional error information
        ('l_IF_number', LONG), # actual interface number
    ]


class ROI_PARAMETERSET(Structure):
    _fields_ = [
        ('lSize', LONG), # size of struct [number of bytes]
        ('lVersion', LONG), # must be 0
        ('usROI', (USHORT * 2) * 2), # 2 ranges, MinIndex and MaxIndex (included)
    ]


class PARAMETERSET(Structure):
    _fields_ = [
        ('lSize', LONG), # size of struct [number of bytes]
        ('lVersion', LONG), # must be 0
        ('dIntTimeAcq', DOUBLE), # integration time for acquisition [ms], <0: use current value
        ('dIntTimeDel', DOUBLE), # integration time for deleting (for sensor work modes with separate integration time for cleaning) [ms], <0: use current value
        ('lAverageBurstNum', LONG), # number of spectra (Average / Burst), -1: use current value
        ('lAverageBurstMode', LONG), # 0: Average (default), 1: Burst, -1: use current value
        ('lBurstTriggerNum', LONG), # -1: Default = 1
        ('lSensorWorkMode', LONG), # -1: use current value
        ('lSensorWorkModeFlags', LONG), #  <=0: Default = none, SWM_SUPPRESS_FIFO_OVERFLOW_PROT = 2
        ('lTriggerTimeout', LONG), # timeout time [ms]
        ('lHWFlashModeEnable', LONG), # 0: off, 1: on, -1: use current value
        ('lHWFlashMode', LONG), # 0: trigger flash together with EOS (default), 1: with STSCAN, -1: use current value
    ]    


class PARAMETERSET_EXT(Structure):
    _fields_ = [
        ('lSize', LONG), # size of struct [number of bytes]
        ('lVersion', LONG), # uses nano modes: 1
        ('lSensorWorkMode', LONG), # 
        ('lBurstNum', LONG), # number of spectra (Average / Burst)
        ('lTriggerTimeout', LONG), # timeout time [ms]
        ('lSpecBufferSize', LONG), # 1...256
        ('lNumOfNotifiers', LONG), # 1...50
        ('lReserve', LONG), # must be 0
        ('dIntTimeAcq', DOUBLE), # integration time for acquisition [ms]
    ]


# class TIME_DATE_STRUCT(Structure):
#     _fields_ = [
#         ('sec', USHORT),
#         ('min', USHORT),
#         ('hour', USHORT),
#         ('day', USHORT),
#         ('month', USHORT),
#         ('year', USHORT),
#     ]


class TIMEDATE_EXT(Structure):
    _fields_ = [
        ('usec', USHORT),
        ('msec', USHORT),
        ('sec', USHORT),
        ('min', USHORT),
        ('hour', USHORT),
        ('day', USHORT),
        ('month', USHORT),
        ('year', USHORT),
    ]


class HWSETTINGS(Structure):
    _fields_ = [
        ('l_IFtype', LONG), # interface
        ('l_IBtype', LONG), # (for later use)
        ('l_FEEtype', LONG), # frontend electronic
        ('l_MUXtype', LONG), # multiplexer
        ('l_SENSORnumber', LONG), # number of sensors (1...8(MUX))
        ('l_SENSORtype', LONG), # sensor
        ('l_SENSORsize', LONG), # pixel number
    ]


class HWSETTINGS_EXT(Structure):
    _fields_ = [
        ('l_IF_type', LONG), # interface
        ('l_IB_type', LONG), # (for later use)
        ('l_FEE_type', LONG), # frontend electronic
        ('l_MUX_type', LONG), # multiplexer
        ('l_SENSOR_number', LONG), # number of sensors (1...8(MUX))
        ('l_SENSOR_type', LONG * MAX_CHANNEL_NUMBER), # sensor
        ('l_SENSOR_length', LONG * MAX_CHANNEL_NUMBER), # number of pixel values
        ('l_SENSOR_rows', LONG * MAX_CHANNEL_NUMBER), # number of rows
    ]


class SENSORCONFIG_X(Structure):
    _fields_ = [
        ('sSensorType', SHORT),
        ('sSensorLength', SHORT),
        ('sSensorBinAreas', SHORT),
        ('sSensorPhysRows', SHORT),
    ]


class SENSORCOEFFS_X(Structure):
    _fields_ = [
        ('dC0', DOUBLE),
        ('dC1', DOUBLE),
        ('dC2', DOUBLE),
        ('dC3', DOUBLE),
        ('dC4', DOUBLE),
    ]


class SENSORPARAMS_X(Structure):
    _fields_ = [
        ('lSize', LONG),
        ('scfConfig', SENSORCONFIG_X),
        ('lReserved', LONG),
        ('scoCoeffs', SENSORCOEFFS_X),
    ]

    
class HWSETTINGS_X(Structure):
    _fields_ = [
        ('lSize', LONG),
        ('sIFType', SHORT),
        ('sFEEType', SHORT),
        ('sMUXType', SHORT),
        ('sNumSensorChannels', SHORT),
        ('lReserved', LONG),
        ('scSensor', SENSORCONFIG_X * 16),
    ]

    
class HWSETTINGS_32X(Structure):
    _fields_ = [
        ('lSize', LONG),
        ('sIFType', SHORT),
        ('sFEEType', SHORT),
        ('sMUXType', SHORT),
        ('sNumSensorChannels', SHORT),
        ('lReserved', LONG),
        ('scSensor', SENSORCONFIG_X * 32),
    ]
    

class TEMPERATURE_RESULTS(Structure):
    _fields_ = [
        ('lSize', LONG),
        ('sNumVal', SHORT),
        ('sReserved', SHORT),
        ('sAddress', SHORT * 8),
        ('fTemperature', FLOAT * 8),
    ]


PCI_INITIAL_STARTUP = 0x04
PCI_INITIAL_STARTUP_SUPPRESS_CLOSING = 0x02
SUPPRESS_ERROR_MESSAGES = 0x01


# Warnings
WNG_DISABLE_ALL = 0x00
WNG_ADC_OVERFLOW = 0x01 # default: disabled
WNG_SPEC_BUFFER_OVERFLOW = 0x02 # default: enabled
WNG_FIFO_OVERFLOW = 0x04 # default: enabled (PD-USB01V1)


# LS constants
LS_DEF_TIMEOUT_LAMPS = 80000 # 80 sec
LS_DEF_TIMEOUT_SHUTTER = 1000 # 1 sec
LS_DEF_SWITCH_DELAY = 10000 # 10 sec

LS_HAL_ONLY = 0x01
LS_D2_ONLY = 0x02
LS_HAL_AND_D2 = 0x03
LS_FLASH = 0x04
LS_LASER = 0x05
LS_FAM_BEKHMP = 0x09

LS_FLASH_STATE_MANUALLY = 0x00
LS_FLASH_STATE_REMOTE = 0x01


# shutter control mode
SCM_DEFAULT_OPEN = 0x00
SCM_DEFAULT_CLOSED = 0x01
SCM_DEFAULT_OPEN_V1 = 0x02
SCM_DEFAULT_MODE = SCM_DEFAULT_OPEN


# electronic families
ELC_INTERFACE = 1
ELC_FRONTEND = 2
ELC_MUX = 3
