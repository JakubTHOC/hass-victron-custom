"""Constants for the Victron integration."""
from enum import Enum
from homeassistant.const import (
    PERCENTAGE,
    UnitOfPower,
    UnitOfEnergy,
    ELECTRIC_POTENTIAL_VOLT,
    ELECTRIC_CURRENT_AMPERE,
    FREQUENCY_HERTZ,
    TIME_SECONDS,
    REVOLUTIONS_PER_MINUTE,
    IRRADIATION_WATTS_PER_SQUARE_METER,
    UnitOfTemperature,
    UnitOfVolume,
    UnitOfSpeed,
    UnitOfPressure,
)
 
from homeassistant.components.sensor import SensorStateClass

class DeviceType(Enum):
    GRID = 1
    TANK = 2
    MULTI = 3
    VEBUS = 4


DOMAIN = "victron"

CONF_HOST = "host"
CONF_PORT = "port"
SCAN_REGISTERS = "registers"
CONF_INTERVAL = "interval"
CONF_ADVANCED_OPTIONS = "advanced"
CONF_AC_CURRENT_LIMIT = "ac_current"
CONF_DC_CURRENT_LIMIT = "dc_current"
CONF_DC_SYSTEM_VOLTAGE = "dc_voltage"
CONF_AC_SYSTEM_VOLTAGE = "ac_voltage"

AC_VOLTAGES = { "US": 120, "EU": 230 } # For now only most common voltages supported
DC_VOLTAGES = { "lifepo4_12v": 12, "lifepo4_24v": 24, "lifepo4_48v": 48 } #only 3 volt nominal 4s, 8s and 16s lifepo4 configurations currently supported


class STRING():
    def __init__(self, length=1, read_length=None):
        self.length = length
        self.readLength =  read_length if read_length is not None else length*2

#maybe change to enum Enum('UINT16', 'UINT32')
UINT16 = "uint16"
INT16  = "int16"
UINT32 = "uint32"
INT32  = "int32"

UINT16_MAX = 65535

class EntityType():
    def __init__(self, entityTypeName):
        self.entityTypeName = entityTypeName

class ReadEntityType(EntityType):
    def __init__(self, entityTypeName: str = "read"):
        super().__init__(entityTypeName=entityTypeName)

class TextReadEntityType(ReadEntityType):
    def __init__(self, decodeEnum: Enum):
        super().__init__()
        self.decodeEnum = decodeEnum

class BoolReadEntityType(ReadEntityType):
    def __init__(self) -> None:
        super().__init__(entityTypeName="bool")

class ButtonWriteType(EntityType):
    def __init__(self) -> None:
        super().__init__(entityTypeName="button")

class SwitchWriteType(EntityType):
    def __init__(self) -> None:
        super().__init__(entityTypeName="switch")

class SliderWriteType(EntityType):
    def __init__(self, powerType="", negative: bool=False):
        super().__init__(entityTypeName="slider")
        self.powerType = powerType
        self.negative = negative
    
class SelectWriteType(EntityType):
    def __init__(self, optionsEnum: Enum):
        super().__init__(entityTypeName="select")
        self.options = optionsEnum


class RegisterInfo():
    def __init__(self, register, dataType, unit="", scale=1, entityType: EntityType = ReadEntityType(), step=0) -> None:
        self.register = register
        self.dataType = dataType
        self.unit = unit
        self.scale = scale
        self.step = step
        #Only used for writeable entities
        self.entityType = entityType
        
    def determine_stateclass(self):
        if self.unit == UnitOfEnergy.KILO_WATT_HOUR:
            return SensorStateClass.TOTAL_INCREASING
        elif self.unit == "":
            return None
        else:
            return SensorStateClass.MEASUREMENT

class generic_alarm_ledger(Enum):
    OK = 0
    WARNING = 1
    ALARM = 2
 
class vebus_mode(Enum):
    CHARGER = 1
    INVERTER = 2
    ON = 3
    OFF = 4

class generic_activeinput(Enum):
    AC_INPUT_1 = 0
    AC_INPUT_2 = 1
    DISCONNECTED = 240

class generic_charger_state(Enum):
    OFF = 0
    LOW_POWER = 1
    FAULT = 2
    BULK = 3
    ABSORPTION = 4
    FLOAT = 5
    STORAGE = 6
    EQUALIZE = 7
    PASSTHRU = 8
    INVERTING = 9
    POWER_ASSIST = 10
    POWER_SUPPLY = 11
    EXTERNAL_CONTROL = 252

class vebus_error(Enum):
    OK = 0
    EXTERNAL_PHASE_TRIGGERED_SWITCHOFF = 1
    MK2_TYPE_MISMATCH = 2
    DEVICE_COUNT_MISMATCH = 3
    NO_OTHER_DEVICES = 4
    AC_OVERVOLTAGE_OUT = 5
    DDC_PROGRAM = 6
    BMS_WITHOUT_ASSISTANT_CONNECTED = 7
    TIME_SYNC_MISMATCH = 10
    CANNOT_TRANSMIT = 14
    DONGLE_ABSENT = 16
    MASTER_FAILOVER = 17
    AC_OVERVOLTAGE_SLAVE_OFF = 18
    CANNOT_BE_SLAVE = 22
    SWITCH_OVER_PROTECTION = 24
    FIRMWARE_INCOMPATIBILTIY = 25
    INTERNAL_ERROR = 26

class vebus_charge_state(Enum):
    INITIALIZING = 0
    BULK = 1
    ABSORBPTION = 2
    FLOAT = 3
    STORAGE = 4
    ABSORBPTION_REPEAT = 5
    FORCED_ABSORBPTION = 6
    EQUALISE = 7
    BULK_STOPPED = 8
    UNKNOWN = 9

class solarcharger_mode(Enum):
    ON = 1
    OFF = 4

class solarcharger_state(Enum):
    OFF = 0
    FAULT = 2
    BULK = 3
    ABSORPTION = 4
    FLOAT = 5
    STORAGE = 6
    EQUALIZE = 7
    OTHER_HUB_1 = 11
    EXTERNAL_CONTROL = 252

class solarcharger_equalization_pending(Enum):
    NO = 0
    YES = 1
    ERROR = 2
    UNAVAILABLE = 3

class generic_charger_errorcode(Enum):
    NONE = 0
    TEMPERATURE_HIGH = 1
    VOLTAGE_HIGH = 2
    TEMPERATURE_SENSOR_PLUS_MISWIRED = 3
    TEMPERATURE_SENSOR_MIN_MISWIRED = 4
    TEMPERATURE_SENSOR_DISCONNECTED = 5
    VOLTAGE_SENSE_PLUS_MISWIRED = 6
    VOLTAGE_SENSE_MIN_MISWIRED = 7
    VOLTAGE_SENSE_DISCONNECTED = 8
    VOLTAGE_WIRE_LOSSES_TOO_HIGH = 9
    CHARGER_TEMPERATURE_TOO_HIGH = 17
    CHARGER_OVER_CURRENT = 18
    CHARGER_POLARITY_REVERSED = 19
    BULK_TIME_LIMIT = 20
    CHARGER_TEMPERATURE_SENSOR_MISWIRED = 22
    CHARGER_TEMPERATURE_SENSOR_DISCONNECTED = 23
    INPUT_CURRENT_TOO_HIGH = 34

class generic_mppoperationmode(Enum):
    OFF = 0
    LIMITED = 1
    ACTIVE = 2
    UNAVAILABLE = 255

class charger_mode(Enum):
    OFF = 0
    ON = 1
    ERROR = 2
    UNAVAILABLE = 3

class ess_mode(Enum):
    ESS_PHASE_COMPENSATION = 1
    ESS_NO_PHASE_COMPENSATION = 2
    EXTERNAL_CONTROL = 3

class generic_status(Enum):
    OK = 0
    DISCONNECTED = 1
    SHORT_CIRCUITED = 2
    REVERSE_POLARITY = 3
    UNKNOWN = 4

class register_input_source(Enum):
    UNKNOWN = 0
    GRID = 1
    GENERATOR = 2
    SHORE = 3
    NOT_CONNECTED = 240


vebus_registers = { 
    "Input voltage": RegisterInfo(3, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
    "Input current": RegisterInfo(6, INT16, ELECTRIC_CURRENT_AMPERE, 10),
    "Input frequency": RegisterInfo(9, INT16, FREQUENCY_HERTZ, 100),
    "Input power": RegisterInfo(12, INT16, UnitOfPower.WATT, 0.1), # could be either POWER_WATT or POWER_VOLT_AMPERE W was chosen
    "Output voltage": RegisterInfo(15, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
    "Output current": RegisterInfo(18, INT16, ELECTRIC_CURRENT_AMPERE, 10),
    "Output frequency": RegisterInfo(21, INT16, FREQUENCY_HERTZ, 100),
    "Active input current limit": RegisterInfo(22, INT16, ELECTRIC_CURRENT_AMPERE, 10, SliderWriteType("AC", True)),
    "Output power": RegisterInfo(23, INT16, UnitOfPower.WATT, 0.1),
    "Battery voltage": RegisterInfo(26, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
    "Battery current": RegisterInfo(27, INT16, ELECTRIC_CURRENT_AMPERE, 10),
    "Active input": RegisterInfo(register=29, dataType=UINT16, entityType=TextReadEntityType(generic_activeinput)),
    "VE.Bus state of charge": RegisterInfo(30, UINT16, PERCENTAGE, 10, SliderWriteType()),
    "VE.Bus state": RegisterInfo(register=31, dataType=UINT16, entityType=TextReadEntityType(generic_charger_state)), #This has no unit of measurement
    "VE.Bus Error": RegisterInfo(register=32, dataType=UINT16, entityType=TextReadEntityType(vebus_error)), #This has no unit of measurement
    "Switch Position": RegisterInfo(register=33, dataType=UINT16, entityType=SelectWriteType(vebus_mode)), #This has no unit of measurement
    "Temperature alarm": RegisterInfo(register=34, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)), #This has no unit of measurement
    "Low battery alarm": RegisterInfo(register=35, dataType=UINT16,  entityType=TextReadEntityType(generic_alarm_ledger)), #This has no unit of measurement
    "Overload alarm": RegisterInfo(register=36,dataType=UINT16,  entityType=TextReadEntityType(generic_alarm_ledger)), #This has no unit of measurement
    "ESS power setpoint": RegisterInfo(register=37, dataType=INT16, unit=UnitOfPower.WATT, entityType=SliderWriteType("AC", True)),
    "ESS disable charge flag phase": RegisterInfo(register=38, dataType=UINT16, entityType=SwitchWriteType()), #This has no unit of measurement
    "ESS disable feedback flag phase": RegisterInfo(39, UINT16, entityType=SwitchWriteType()), #This has no unit of measurement
    "Temperatur sensor alarm": RegisterInfo(register=42, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)), #This has no unit of measurement
    "Voltage sensor alarm": RegisterInfo(register=43, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)), #This has no unit of measurement
    "Temperature alarm": RegisterInfo(register=44, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)), #This has no unit of measurement
    "Low battery alarm": RegisterInfo(register=45, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)), #This has no unit of measurement
    "Overload alarm": RegisterInfo(register=46, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)), #This has no unit of measurement
    "Ripple alarm": RegisterInfo(register=47, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)), #This has no unit of measurement
    "Disable PV inverter": RegisterInfo(register=56, dataType=UINT16, entityType=SwitchWriteType()), #This has no unit of measurement
    "VE.Bus BMS allows battery to be charged": RegisterInfo(register=57, dataType=UINT16, entityType=BoolReadEntityType()), #This has no unit of measurement
    "VE.Bus BMS allows battery to be discharged": RegisterInfo(register=58, dataType=UINT16, entityType=BoolReadEntityType()), #This has no unit of measurement
    "VE.Bus BMS is expected": RegisterInfo(register=59, dataType=UINT16, entityType=BoolReadEntityType()), #This has no unit of measurement
    "VE.Bus BMS error": RegisterInfo(register=60, dataType=UINT16, entityType=BoolReadEntityType()), #This has no unit of measurement
    "Battery temperature": RegisterInfo(61, INT16, UnitOfTemperature.CELSIUS, 10),
    "VE.Bus Reset": RegisterInfo(register=62, dataType=UINT16, entityType=ButtonWriteType()), #This has no unit of measurement
    "Grid lost alarm": RegisterInfo(register=64, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)), #This has no unit of measurement
    "Feed DC overvoltage into grid": RegisterInfo(register=65, dataType=UINT16, entityType=SwitchWriteType()), #This has no unit of measurement
    "Maximum overvoltage feed-in power": RegisterInfo(66, UINT16, UnitOfPower.WATT, 0.01, SliderWriteType("AC", False)),
    "AC input 1 ignored": RegisterInfo(register=69, dataType=UINT16, entityType=BoolReadEntityType()), #This has no unit of measurement
    "AC input 2 ignored": RegisterInfo(register=70, dataType=UINT16, entityType=BoolReadEntityType()), #This has no unit of measurement
    "AcPowerSetpoint acts as feed-in limit": RegisterInfo(register=71, dataType=UINT16, entityType=SwitchWriteType()), #This has no unit of measurement
    "Solar offset voltage": RegisterInfo(register=72, dataType=UINT16, entityType=SwitchWriteType()), #This has no unit of measurement
    "Sustain active": RegisterInfo(register=73, dataType=UINT16, entityType=BoolReadEntityType()), #This has no unit of measurement
    "Energy from AC-In 1 to AC-out": RegisterInfo(74, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    "Energy from AC-In 1 to battery": RegisterInfo(76, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    "Energy from AC-In 2 to AC-out": RegisterInfo(78, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    "Energy from AC-In 2 to battery": RegisterInfo(80, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    "Energy from AC-out to AC-in 1 (reverse fed PV)": RegisterInfo(82, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    "Energy from AC-out to AC-in 2 (reverse fed PV)": RegisterInfo(84, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    "Energy from battery to AC-in 1": RegisterInfo(86, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    "Energy from battery to AC-in 2": RegisterInfo(88, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    "Energy from battery to AC-out": RegisterInfo(90, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    "Energy from AC-out to battery (typically from PV-inverter)": RegisterInfo(92, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # "Low cell voltage imminent": RegisterInfo(94, UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "Charge state": RegisterInfo(register=95, dataType=UINT16, entityType=TextReadEntityType(vebus_charge_state))
}

solarcharger_registers = {
    # "Battery voltage": RegisterInfo(771, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
    "Battery current": RegisterInfo(772, INT16, ELECTRIC_CURRENT_AMPERE, 10),
    "Battery temperature": RegisterInfo(773, INT16, UnitOfTemperature.CELSIUS, 10),
    # "Charger on/off": RegisterInfo(register=774, dataType=UINT16, entityType=SelectWriteType(solarcharger_mode)),
    "Charge state": RegisterInfo(register=775, dataType=UINT16, entityType=TextReadEntityType(solarcharger_state)),
    "PV voltage": RegisterInfo(776, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
    "PV current": RegisterInfo(777, INT16, ELECTRIC_CURRENT_AMPERE, 10),
    "Equalization pending": RegisterInfo(register=778, dataType=UINT16, entityType=TextReadEntityType(solarcharger_equalization_pending)),
    "Equalization time remaining": RegisterInfo(779, UINT16, TIME_SECONDS, 10),
    "Relay on the charger": RegisterInfo(register=780, dataType=UINT16, entityType=BoolReadEntityType()),
    "Solarcharger Alarm": RegisterInfo(register=781, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    "Low batt. voltage alarm": RegisterInfo(register=782, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    "High batt. voltage alarm": RegisterInfo(register=783, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    "Yield today": RegisterInfo(784, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
    "Maximum charge power today": RegisterInfo(785, UINT16, UnitOfPower.WATT),
    "Yield yesterday": RegisterInfo(786, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
    "Maximum charge power yesterday": RegisterInfo(787, UINT16, UnitOfPower.WATT),
    "Error code": RegisterInfo(register=788, dataType=UINT16, entityType=TextReadEntityType(generic_charger_errorcode)),
    "PV power": RegisterInfo(789, UINT16, UnitOfPower.WATT, 10),
    "User yield": RegisterInfo(790, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
    "MPP operation mode": RegisterInfo(register=791, dataType=UINT16, entityType=TextReadEntityType(generic_mppoperationmode)),
    "User yield": RegisterInfo(3728, UINT32, UnitOfEnergy.KILO_WATT_HOUR),
    "PV power": RegisterInfo(3730, UINT16, UnitOfPower.WATT)
}


system_registers = {
    "Victron Serial (System)": RegisterInfo(800, STRING(6)),
    "Victron CCGX Relay 1 state": RegisterInfo(register=806, dataType=UINT16, entityType=SwitchWriteType()),
    "Victron CCGX Relay 2 state": RegisterInfo(register=807, dataType=UINT16, entityType=SwitchWriteType()),
    "Victron PV - AC-coupled on output": RegisterInfo(808, UINT16, UnitOfPower.WATT),
    "Victron PV - AC-coupled on input": RegisterInfo(811, UINT16, UnitOfPower.WATT),
    "Victron PV - AC-coupled on generator": RegisterInfo(814, UINT16, UnitOfPower.WATT),
    "Victron AC Consumption": RegisterInfo(817, UINT16, UnitOfPower.WATT),
    "Victron Grid": RegisterInfo(820, INT16, UnitOfPower.WATT),
    "Victron Genset": RegisterInfo(823, INT16, UnitOfPower.WATT),
    "Victron Active input source": RegisterInfo(register=826, dataType=INT16, entityType=TextReadEntityType(register_input_source))
}

valid_unit_ids = [100, 229, 228]

register_info_dict = { 
    "system_registers": system_registers,
    "solarcharger_registers": solarcharger_registers,
    "vebus_registers": vebus_registers


    # "system_dc_registers": system_dc_registers, 
    # "system_charger_registers": system_charger_registers
    # "system_power_registers": system_power_registers
    # "system_bus_registers": system_bus_registers

    # DISBALED
    # "system_battery_registers": system_battery_registers, 
    # "battery_registers": battery_registers, 
    # "battery_detail_registers": battery_detail_registers, 
    # "settings_ess_registers": settings_ess_registers, 
    # "inverter_info_registers": inverter_info_registers,
    # "inverter_energy_registers": inverter_energy_registers, 
    # "inverter_tracker_registers": inverter_tracker_registers, 
    # "inverter_tracker_statistics_registers": inverter_tracker_statistics_registers
    # "solarcharger_tracker_voltage_registers": solarcharger_tracker_voltage_registers,
    # "solarcharger_tracker_registers": solarcharger_tracker_registers, 
    # "pvinverter_registers": pvinverter_registers, 
    # "motordrive_registers": motordrive_registers,
    # "charger_registers": charger_registers, 
    # "settings_registers": settings_registers,
    # "gps_registers": gps_registers, 
    # "gavazi_grid_registers": gavazi_grid_registers,
    # "tank_registers": tank_registers, 
    # "inverter_output_registers": inverter_output_registers,
    # "inverter_battery_registers": inverter_battery_registers, 
    # "inverter_alarm_registers": inverter_alarm_registers, 
    # "genset_registers": genset_registers, 
    # "temperature_registers": temperature_registers, 
    # "pulsemeter_registers": pulsemeter_registers, 
    # "digitalinput_registers": digitalinput_registers,
    # "generator_registers": generator_registers, 
    # "meteo_registers": meteo_registers,
    # "evcharger_productid_registers": evcharger_productid_registers, 
    # "evcharger_registers": evcharger_registers,
    # "acload_registers": acload_registers, 
    # "fuelcell_registers": fuelcell_registers, 
    # "alternator_registers": alternator_registers, 
    # "dcsource_registers": dcsource_registers,
    # "dcload_registers": dcload_registers, 
    # "dcsystem_registers": dcsystem_registers, 
    # "multi_registers": multi_registers, 
}    


# DISBLED

# system_dc_registers = {
    # "PV - DC-coupled power": RegisterInfo(850, UINT16, UnitOfPower.WATT),
    # "PV - DC-coupled current": RegisterInfo(851, INT16, ELECTRIC_CURRENT_AMPERE, 10)
# }

# system_charger_registers = {
    # "Charger power": RegisterInfo(855, UINT16, UnitOfPower.WATT)
# }

# system_bus_registers = {
#     "VE.Bus charge current (System)": RegisterInfo(865, INT16, ELECTRIC_CURRENT_AMPERE, 10),
#     "VE.Bus charge power (System)": RegisterInfo(866, INT16, UnitOfPower.WATT)
# }

# system_power_registers = {
#     "DC System Power": RegisterInfo(860, INT16, UnitOfPower.WATT)
# }

# gavazi_grid_registers = { 
#     "grid_L1_power": RegisterInfo(2600, INT16, UnitOfPower.WATT),
#     # "grid_L2_power": RegisterInfo(2601, INT16, UnitOfPower.WATT),
#     # "grid_L3_power": RegisterInfo(2602, INT16, UnitOfPower.WATT),
#     "grid_L1_energy_forward": RegisterInfo(2603, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 100),
#     # "grid_L3_energy_forward": RegisterInfo(2605, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 100),
#     # "grid_L2_energy_forward": RegisterInfo(2604, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 100),
#     "grid_L1_energy_reverse": RegisterInfo(2606, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 100),
#     # "grid_L2_energy_reverse": RegisterInfo(2607, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 100),
#     # "grid_L3_energy_reverse": RegisterInfo(2608, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 100),
#     "grid_serial": RegisterInfo(2609, STRING(7)),
#     "grid_L1_voltage": RegisterInfo(2616, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
#     "grid_L1_current": RegisterInfo(2617, INT16, ELECTRIC_CURRENT_AMPERE, 10),
#     # "grid_L2_voltage": RegisterInfo(2618, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
#     # "grid_L2_current": RegisterInfo(2619, INT16, ELECTRIC_CURRENT_AMPERE, 10),
#     # "grid_L3_voltage": RegisterInfo(2620, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
#     # "grid_L3_current": RegisterInfo(2621, INT16, ELECTRIC_CURRENT_AMPERE, 10),
#     "grid_L1_energy_forward_total": RegisterInfo(2622, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
#     # "grid_L2_energy_forward_total": RegisterInfo(2624, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
#     # "grid_L3_energy_forward_total": RegisterInfo(2626, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
#     "grid_L1_energy_reverse_total": RegisterInfo(2628, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
#     # "grid_L2_energy_reverse_total": RegisterInfo(2630, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
#     # "grid_L3_energy_reverse_total": RegisterInfo(2632, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
#     "grid_energy_forward_total": RegisterInfo(2634, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
#     "grid_energy_reverse_total": RegisterInfo(2636, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100)
# }

# multi_registers = {
    # "multi_input_L1_voltage": RegisterInfo(4500, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
    # # "multi_input_L2_voltage": RegisterInfo(4501, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
    # # "multi_input_L3_voltage": RegisterInfo(4502, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
    # "multi_input_L1_current": RegisterInfo(4503, UINT16, ELECTRIC_CURRENT_AMPERE, 10),
    # # "multi_input_L2_current": RegisterInfo(4504, UINT16, ELECTRIC_CURRENT_AMPERE, 10),
    # # "multi_input_L3_current": RegisterInfo(4505, UINT16, ELECTRIC_CURRENT_AMPERE, 10),
    # "multi_input_L1_power": RegisterInfo(4506, INT16, UnitOfPower.WATT, 0.1),
    # "multi_input_L2_power": RegisterInfo(4507, INT16, UnitOfPower.WATT, 0.1),
    # "multi_input_L3_power": RegisterInfo(4508, INT16, UnitOfPower.WATT, 0.1),
    # "multi_input_L1_frequency": RegisterInfo(4509, UINT16, FREQUENCY_HERTZ, 100),
    # "multi_output_L1_voltage": RegisterInfo(4510, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
    # # "multi_output_L2_voltage": RegisterInfo(4511, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
    # # "multi_output_L3_voltage": RegisterInfo(4512, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
    # "multi_output_L1_current": RegisterInfo(4513, UINT16, ELECTRIC_CURRENT_AMPERE, 10),
    # # "multi_output_L2_current": RegisterInfo(4514, UINT16, ELECTRIC_CURRENT_AMPERE, 10),
    # # "multi_output_L3_current": RegisterInfo(4515, UINT16, ELECTRIC_CURRENT_AMPERE, 10),
    # "multi_output_L1_power": RegisterInfo(4516, INT16, UnitOfPower.WATT, 0.1),
    # "multi_output_L2_power": RegisterInfo(4517, INT16, UnitOfPower.WATT, 0.1),
    # "multi_output_L3_power": RegisterInfo(4518, INT16, UnitOfPower.WATT, 0.1),
    # "multi_output_L1_frequency": RegisterInfo(4519, UINT16, FREQUENCY_HERTZ, 100),
    # "multi_input_1_type": RegisterInfo(register=4520, dataType=UINT16, entityType=TextReadEntityType(multi_input_type)),
    # "multi_input_2_type": RegisterInfo(register=4521, dataType=UINT16, entityType=TextReadEntityType(multi_input_type)),
    # "multi_input_1_currentlimit": RegisterInfo(4522, UINT16, ELECTRIC_CURRENT_AMPERE, 10, SliderWriteType("AC", False)),
    # "multi_input_2_currentlimit": RegisterInfo(4523, UINT16, ELECTRIC_CURRENT_AMPERE, 10, SliderWriteType("AC", False)),
    # "multi_numberofphases": RegisterInfo(4524, UINT16),
    # "multi_activein_activeinput": RegisterInfo(register=4525, dataType=UINT16, entityType=TextReadEntityType(generic_activeinput)),
    # "multi_battery_voltage": RegisterInfo(4526, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
    # "multi_battery_current": RegisterInfo(4527, INT16, ELECTRIC_CURRENT_AMPERE, 10),
    # "multi_battery_temperature": RegisterInfo(4528, INT16, UnitOfTemperature.CELSIUS, 10),
    # "multi_battery_soc": RegisterInfo(4529, UINT16, PERCENTAGE, 10),
    # "multi_state": RegisterInfo(register=4530, dataType=UINT16, entityType=TextReadEntityType(generic_charger_state)),
    # "multi_mode": RegisterInfo(register=4531, dataType=UINT16, entityType=SelectWriteType(multi_mode)),
    # "multi_alarm_hightemperature": RegisterInfo(register=4532, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "multi_alarm_highvoltage": RegisterInfo(register=4533, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "multi_alarm_highvoltageacout": RegisterInfo(register=4534, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "multi_alarm_lowtemperature": RegisterInfo(register=4535, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "multi_alarm_lowvoltage": RegisterInfo(register=4536, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "multi_alarm_lowvoltageacout": RegisterInfo(register=4537, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "multi_alarm_overload": RegisterInfo(register=4538, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "multi_alarm_ripple": RegisterInfo(register=4539, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "multi_yield_pv_power": RegisterInfo(4540, UINT16, UnitOfPower.WATT),
    # "multi_yield_user": RegisterInfo(4541, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
    # "multi_relay": RegisterInfo(register=4542, dataType=UINT16, entityType=BoolReadEntityType()),
    # "multi_mppoperationmode": RegisterInfo(register=4543, dataType=UINT16, entityType=TextReadEntityType(generic_mppoperationmode)),
    # "multi_pv_voltage": RegisterInfo(4544, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
    # "multi_errorcode": RegisterInfo(register=4545, dataType=UINT16, entityType=TextReadEntityType(generic_charger_errorcode)),
    # "multi_energy_acin1toacout": RegisterInfo(4546, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # "multi_energy_acin1toinverter": RegisterInfo(4548, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # "multi_energy_acin2toacout": RegisterInfo(4550, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # "multi_energy_acin2toinverter": RegisterInfo(4552, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # "multi_energy_acouttoacin1": RegisterInfo(4554, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # "multi_energy_acouttoacin2": RegisterInfo(4556, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # "multi_energy_invertertoacin1": RegisterInfo(4558, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # "multi_energy_invertertoacin2": RegisterInfo(4560, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # "multi_energy_invertertoacout": RegisterInfo(4562, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # "multi_energy_outtoinverter": RegisterInfo(4564, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # "multi_energy_solartoacin1": RegisterInfo(4566, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # "multi_energy_solartoacin2": RegisterInfo(4568, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # "multi_energy_solartoacout": RegisterInfo(4570, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # "mutli_energy_solartobattery": RegisterInfo(4572, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # "multi_history_yield_today": RegisterInfo(4574, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
    # "multi_history_maxpower_today": RegisterInfo(4575, UINT16, UnitOfPower.WATT),
    # "multi_history_yield_yesterday": RegisterInfo(4576, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
    # "multi_history_maxpower_yesterday": RegisterInfo(4577, UINT16, UnitOfPower.WATT),
    # "multi_history_tracker_0_yield_today": RegisterInfo(4578, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
    # "multi_history_tracker_1_yield_today": RegisterInfo(4579, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
    # "multi_history_tracker_2_yield_today": RegisterInfo(4580, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
    # "multi_history_tracker_3_yield_today": RegisterInfo(4581, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
    # "multi_history_tracker_0_yield_yesterday": RegisterInfo(4582, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
    # "multi_history_tracker_1_yield_yesterday": RegisterInfo(4583, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
    # "multi_history_tracker_2_yield_yesterday": RegisterInfo(4584, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
    # "multi_history_tracker_3_yield_yesterday": RegisterInfo(4585, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
    # "multi_history_tracker_0_maxpower_today": RegisterInfo(4586, UINT16, UnitOfPower.WATT),
    # "multi_history_tracker_1_maxpower_today": RegisterInfo(4587, UINT16, UnitOfPower.WATT),
    # "multi_history_tracker_2_maxpower_today": RegisterInfo(4588, UINT16, UnitOfPower.WATT),
    # "multi_history_tracker_3_maxpower_today": RegisterInfo(4589, UINT16, UnitOfPower.WATT),
    # "multi_history_tracker_0_maxpower_yesterday": RegisterInfo(4590, UINT16, UnitOfPower.WATT),
    # "multi_history_tracker_1_maxpower_yesterday": RegisterInfo(4591, UINT16, UnitOfPower.WATT),
    # "multi_history_tracker_2_maxpower_yesterday": RegisterInfo(4592, UINT16, UnitOfPower.WATT),
    # "multi_history_tracker_3_maxpower_yesterday": RegisterInfo(4593, UINT16, UnitOfPower.WATT),
    # "multi_tracker_0_voltage": RegisterInfo(4594, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
    # "multi_tracker_1_voltage": RegisterInfo(4595, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
    # "multi_tracker_2_voltage": RegisterInfo(4596, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
    # "multi_tracker_3_voltage": RegisterInfo(4597, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
    # "multi_tracker_0_power": RegisterInfo(4598, UINT16, UnitOfPower.WATT),
    # "multi_tracker_1_power": RegisterInfo(4599, UINT16, UnitOfPower.WATT),
    # "multi_tracker_2_power": RegisterInfo(4600, UINT16, UnitOfPower.WATT),
    # "multi_tracker_3_power": RegisterInfo(4601, UINT16, UnitOfPower.WATT),
    # "multi_alarm_lowsoc": RegisterInfo(register=4602, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger))

# }

# evcharger_registers = {
    # "evcharger_firmwareversion": RegisterInfo(3802, UINT32),
    # "evcharger_serial": RegisterInfo(3804, STRING(6)),
    # "evcharger_model": RegisterInfo(3810, STRING(4)),
    # "evcharger_maxcurrent": RegisterInfo(register=3814, dataType=UINT16, unit=ELECTRIC_CURRENT_AMPERE, entityType=SliderWriteType("AC", False)),
    # "evcharger_mode": RegisterInfo(register=3815, dataType=UINT16, entityType=SelectWriteType(evcharger_mode)),
    # "evcharger_energy_forward": RegisterInfo(3816, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # "evcharger_L1_power": RegisterInfo(3818, UINT16, UnitOfPower.WATT),
    # "evcharger_L2_power": RegisterInfo(3819, UINT16, UnitOfPower.WATT),
    # "evcharger_L3_power": RegisterInfo(3820, UINT16, UnitOfPower.WATT),
    # "evcharger_total_power": RegisterInfo(3821, UINT16, UnitOfPower.WATT),
    # "evcharger_chargingtime": RegisterInfo(3822, UINT16, TIME_SECONDS, 0.01),
    # "evcharger_current": RegisterInfo(3823, UINT16, ELECTRIC_CURRENT_AMPERE),
    # "evcharger_status": RegisterInfo(register=3824, dataType=UINT16, entityType=TextReadEntityType(evcharger_status)),
    # "evcharger_setcurrent": RegisterInfo(register=3825, dataType=UINT16, unit=ELECTRIC_CURRENT_AMPERE, entityType=SliderWriteType("AC", False)),
    # "evcharger_startstop": RegisterInfo(register=3826, dataType=UINT16, entityType=SwitchWriteType()),
    # "evcharger_position": RegisterInfo(register=3827, dataType=UINT16, entityType=TextReadEntityType(generic_position)),
# }

# acload_registers = {
    # "acload_L1_power": RegisterInfo(3900, UINT16, UnitOfPower.WATT),
    # # "acload_L2_power": RegisterInfo(3901, UINT16, UnitOfPower.WATT),
    # # "acload_L3_power": RegisterInfo(3902, UINT16, UnitOfPower.WATT),
    # "acload_serial": RegisterInfo(3903, STRING(7)),
    # "acload_L1_voltage": RegisterInfo(3910, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
    # "acload_L1_current": RegisterInfo(3911, INT16, ELECTRIC_CURRENT_AMPERE, 10),
    # # "acload_L2_voltage": RegisterInfo(3912, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
    # # "acload_L2_current": RegisterInfo(3913, INT16, ELECTRIC_CURRENT_AMPERE, 10),
    # # "acload_L3_voltage": RegisterInfo(3914, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
    # # "acload_L3_current": RegisterInfo(3915, INT16, ELECTRIC_CURRENT_AMPERE, 10),
    # "acload_L1_energy_forward": RegisterInfo(3916, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # # "acload_L2_energy_forward": RegisterInfo(3918, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # # "acload_L3_energy_forward": RegisterInfo(3920, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100)
# }

# fuelcell_registers = {
    # "fuelcell_battery_voltage": RegisterInfo(4000, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
    # "fuelcell_battery_current": RegisterInfo(4001, INT16, ELECTRIC_CURRENT_AMPERE, 10),
    # "fuelcell_starter_voltage": RegisterInfo(4002, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
    # "fuelcell_temperature": RegisterInfo(4003, INT16, UnitOfTemperature.CELSIUS, 10),
    # "fuelcell_history_energyout": RegisterInfo(4004, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # "fuelcell_alarm_lowvoltage": RegisterInfo(register=4006, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "fuelcell_alarm_highvoltage": RegisterInfo(register=4007, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "fuelcell_alarm_lowstartervoltage": RegisterInfo(register=4008, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "fuelcell_alarm_highstartervoltage": RegisterInfo(register=4009, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "fuelcell_alarm_lowtemperature": RegisterInfo(register=4010, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "fuelcell_alarm_hightemperature": RegisterInfo(register=4011, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger))
# }

# generator_registers = {
    # "generator_manualstart": RegisterInfo(register=3500, dataType=UINT16, entityType=SwitchWriteType()),
    # "generator_runningbyconditioncode": RegisterInfo(register=3501, dataType=UINT16, entityType=TextReadEntityType(generator_runningbyconditioncode)),
    # "generator_runtime": RegisterInfo(3502, UINT16, TIME_SECONDS),
    # "generator_quiethours": RegisterInfo(register=3503, dataType=UINT16, entityType=BoolReadEntityType()),
    # "generator_runtime_2": RegisterInfo(3504, UINT32, TIME_SECONDS),
    # "generator_state": RegisterInfo(register=3506, dataType=UINT16, entityType=TextReadEntityType(generator_state)),
    # "generator_error": RegisterInfo(register=3507, dataType=UINT16, entityType=TextReadEntityType(generator_error)),
    # "generator_alarm_nogeneratoratacin": RegisterInfo(register=3508, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "generator_autostartenabled": RegisterInfo(register=3509, dataType=UINT16, entityType=SwitchWriteType())
# }

#not processed yet
# meteo_registers = {
    # "meteo_irradiance": RegisterInfo(3600, UINT16, IRRADIATION_WATTS_PER_SQUARE_METER, 10),
    # "meteo_windspeed": RegisterInfo(3601, UINT16, UnitOfSpeed.METERS_PER_SECOND, 10),
    # "meteo_celltemperature": RegisterInfo(3602, INT16, UnitOfTemperature.CELSIUS, 10),
    # "meteo_externaltemperature": RegisterInfo(3603, INT16, UnitOfTemperature.CELSIUS, 10)
# }

# evcharger_productid_registers = {
#     "evcharger_productid": RegisterInfo(3800, UINT16)
# }
# alternator_registers = {
    # "alternator_battery_voltage": RegisterInfo(4100, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
    # "alternator_battery_current": RegisterInfo(4101, INT16, ELECTRIC_CURRENT_AMPERE, 10),
    # "alternator_startervoltage": RegisterInfo(4102, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
    # "alternator_temperature": RegisterInfo(4103, INT16, UnitOfTemperature.CELSIUS, 10),
    # "alternator_history_energyout": RegisterInfo(4104, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # "alternator_alarm_lowvoltage": RegisterInfo(register=4106, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "alternator_alarm_highvoltage": RegisterInfo(register=4107, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "alternator_alarm_lowstartervoltage": RegisterInfo(register=4108, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "alternator_alarm_highstartervoltage": RegisterInfo(register=4109, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "alternator_alarm_lowtemperature": RegisterInfo(register=4110, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "alternator_alarm_hightemperature": RegisterInfo(register=4111, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "alternator_state": RegisterInfo(register=4112, dataType=UINT16, entityType=TextReadEntityType(alternator_state)),
    # "alternator_errorcode": RegisterInfo(register=4113, dataType=UINT16, entityType=TextReadEntityType(alternator_errorcode)),
    # "alternator_engine_speed": RegisterInfo(4114, UINT16, REVOLUTIONS_PER_MINUTE),
    # "alternator_alternator_speed": RegisterInfo(4115, UINT16, REVOLUTIONS_PER_MINUTE),
    # "alternator_fielddrive": RegisterInfo(4116, UINT16, PERCENTAGE)
# }

# dcsource_registers = {
    # "dcsource_battery_voltage": RegisterInfo(4200, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
    # "dcsource_battery_current": RegisterInfo(4201, INT16, ELECTRIC_CURRENT_AMPERE, 10),
    # "dcsource_starter_voltage": RegisterInfo(4202, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
    # "dcsource_temperature": RegisterInfo(4203, INT16, UnitOfTemperature.CELSIUS, 10),
    # "dcsource_history_energyout": RegisterInfo(4204, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # "dcsource_alarm_lowvoltage": RegisterInfo(register=4206, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "dcsource_alarm_highvoltage": RegisterInfo(register=4207, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "dcsource_alarm_lowstartervoltage": RegisterInfo(register=4208, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "dcsource_alarm_highstartervoltage": RegisterInfo(register=4209, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "dcsource_alarm_lowtemperature": RegisterInfo(register=4210, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "dcsource_alarm_hightemperature": RegisterInfo(register=4211, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
# }

# dcload_registers = {
    # "dcload_battery_voltage": RegisterInfo(4300, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
    # "dcload_battery_current": RegisterInfo(4301, INT16, ELECTRIC_CURRENT_AMPERE, 10),
    # "dcload_starter_voltage": RegisterInfo(4302, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
    # "dcload_temperature": RegisterInfo(4303, INT16, UnitOfTemperature.CELSIUS, 10),
    # "dcload_history_energyin": RegisterInfo(4304, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # "dcload_alarm_lowvoltage": RegisterInfo(register=4306, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "dcload_alarm_highvoltage": RegisterInfo(register=4307, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "dcload_alarm_lowstartervoltage": RegisterInfo(register=4308, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "dcload_alarm_highstartervoltage": RegisterInfo(register=4309, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "dcload_alarm_lowtemperature": RegisterInfo(register=4310, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "dcload_alarm_hightemperature": RegisterInfo(register=4311, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger))
# }

# dcsystem_registers = {
    # "dcsystem_battery_voltage": RegisterInfo(4400, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
    # "dcsystem_battery_current": RegisterInfo(4401, INT16, ELECTRIC_CURRENT_AMPERE, 10),
    # "dcsystem_starter_voltage": RegisterInfo(4402, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
    # "dcsystem_temperature": RegisterInfo(4403, INT16, UnitOfTemperature.CELSIUS, 10),
    # "dcsystem_history_energyout": RegisterInfo(4404, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # "dcsystem_history_energyin": RegisterInfo(4406, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
    # "dcsystem_alarm_lowvoltage": RegisterInfo(register=4408, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "dcsystem_alarm_highvoltage": RegisterInfo(register=4409, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "dcsystem_alarm_lowstartervoltage": RegisterInfo(register=4410, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "dcsystem_alarm_highstartervoltage": RegisterInfo(register=4411, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "dcsystem_alarm_lowtemperature": RegisterInfo(register=4412, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "dcsystem_alarm_hightemperature": RegisterInfo(register=4413, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger))
# }

# digitalinput_registers = {
    # "digitalinput_count": RegisterInfo(3420, UINT32),
    # "digitalinput_state": RegisterInfo(register=3422, dataType=UINT16, entityType=TextReadEntityType(digitalinput_state)),
    # "digitalinput_alarm": RegisterInfo(register=3423, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "digitalinput_type": RegisterInfo(register=3424, dataType=UINT16, entityType=TextReadEntityType(digitalinput_type))
# }


# temperature_registers = {
    # "temperature_productid": RegisterInfo(3300, UINT16),
    # "temperature_scale": RegisterInfo(3301, UINT16, "", 100),
    # "temperature_offset": RegisterInfo(3302, INT16, "",100),
    # "temperature_type": RegisterInfo(register=3303, dataType=UINT16, entityType=TextReadEntityType(temperature_type)),
    # "temperature_temperature": RegisterInfo(3304, INT16, UnitOfTemperature.CELSIUS, 100),
    # "temperature_status": RegisterInfo(register=3305, dataType=UINT16, entityType=TextReadEntityType(generic_status)),
    # "temperature_humidity": RegisterInfo(3306, UINT16, PERCENTAGE, 10),
    # "temperature_batteryvoltage": RegisterInfo(3307, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
    # "temperature_pressure": RegisterInfo(3308, UINT16, UnitOfPressure.HPA)
# }

# pulsemeter_registers = {
    # "pulsemeter_aggregate": RegisterInfo(3400, UINT32, UnitOfVolume.CUBIC_METERS),
    # "pulsemeter_count": RegisterInfo(3402, UINT32)
# }

# genset_registers = {
    # "genset_L1_voltage": RegisterInfo(3200, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
    # "genset_L2_voltage": RegisterInfo(3201, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
    # "genset_L3_voltage": RegisterInfo(3202, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
    # "genset_L1_current": RegisterInfo(3203, INT16, ELECTRIC_CURRENT_AMPERE, 10),
    # "genset_L2_current": RegisterInfo(3204, INT16, ELECTRIC_CURRENT_AMPERE, 10),
    # "genset_L3_current": RegisterInfo(3205, INT16, ELECTRIC_CURRENT_AMPERE, 10),
    # "genset_L1_power": RegisterInfo(3206, INT16, UnitOfPower.WATT),
    # "genset_L2_power": RegisterInfo(3207, INT16, UnitOfPower.WATT),
    # "genset_L3_power": RegisterInfo(3208, INT16, UnitOfPower.WATT),
    # "genset_L1_frequency": RegisterInfo(3209, UINT16, FREQUENCY_HERTZ, 100),
    # "genset_L2_frequency": RegisterInfo(3210, UINT16, FREQUENCY_HERTZ, 100),
    # "genset_L3_frequency": RegisterInfo(3211, UINT16, FREQUENCY_HERTZ, 100),
    # "genset_productid": RegisterInfo(3212, UINT16),
    # "genset_statuscode": RegisterInfo(register=3213, dataType=UINT16, entityType=TextReadEntityType(genset_status)),
    # "genset_errorcode": RegisterInfo(register=3214, dataType=UINT16, entityType=TextReadEntityType(genset_errorcode)),
    # "genset_autostart": RegisterInfo(register=3215, dataType=UINT16, entityType=BoolReadEntityType()),
    # "genset_engine_load": RegisterInfo(3216, UINT16, PERCENTAGE),
    # "genset_engine_speed": RegisterInfo(3217, UINT16, REVOLUTIONS_PER_MINUTE),
    # "genset_engine_operatinghours": RegisterInfo(3218, UINT16, TIME_SECONDS, 0.01),
    # "genset_engine_coolanttemperature": RegisterInfo(3219, INT16, UnitOfTemperature.CELSIUS, 10),
    # "genset_engine_windingtemperature": RegisterInfo(3220, INT16, UnitOfTemperature.CELSIUS, 10),
    # "genset_engine_exhausttemperature": RegisterInfo(3221, INT16, UnitOfTemperature.CELSIUS, 10),
    # "genset_startervoltage": RegisterInfo(3222, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
    # "genset_start": RegisterInfo(register=3223, dataType=UINT16, entityType=SwitchWriteType())
# }

# tank_registers = {
#     # "tank_productid": RegisterInfo(3000, UINT16),
#     # "tank_capacity": RegisterInfo(3001, UINT32, UnitOfVolume.CUBIC_METERS, 10000),
#     # "tank_fluidtype": RegisterInfo(register=3003, dataType=UINT16, entityType=TextReadEntityType(tank_fluidtype)),
#     # "tank_level": RegisterInfo(3004, UINT16, PERCENTAGE, 10),
#     # "tank_remaining": RegisterInfo(3005, UINT32, UnitOfVolume.CUBIC_METERS, 10000),
#     # "tank_status": RegisterInfo(register=3007, dataType=UINT16, entityType=TextReadEntityType(generic_status))
# }

# inverter_output_registers = {
#     # "inverter_output_L1_current": RegisterInfo(3100, INT16, ELECTRIC_CURRENT_AMPERE, 10),
#     # "inverter_output_L1_voltage": RegisterInfo(3101, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
#     # "inverter_output_L1_power": RegisterInfo(3102, INT16, UnitOfPower.WATT, 0.1),
# }

# inverter_battery_registers = {
#     "inverter_battery_voltage": RegisterInfo(3105, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
#     "inverter_battery_current": RegisterInfo(3106, INT16, ELECTRIC_CURRENT_AMPERE, 10),
# }

# inverter_alarm_registers = {
#     "inverter_alarm_hightemperature": RegisterInfo(register=3110, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "inverter_alarm_highbatteryvoltage": RegisterInfo(register=3111, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "inverter_alarm_highacoutvoltage": RegisterInfo(register=3112, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "inverter_alarm_lowtemperature": RegisterInfo(register=3113, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "inverter_alarm_lowbatteryvoltage": RegisterInfo(register=3114, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "inverter_alarm_lowacoutvoltage": RegisterInfo(register=3115, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "inverter_alarm_overload": RegisterInfo(register=3116, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "inverter_alarm_ripple": RegisterInfo(register=3117, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
# }


# charger_registers = {
    # "charger_voltage_output_1": RegisterInfo(2307, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
    # "charger_current_output_1": RegisterInfo(2308, INT16, ELECTRIC_CURRENT_AMPERE, 10),
    # "charger_temperature": RegisterInfo(2309, INT16, UnitOfTemperature.CELSIUS, 10),
    # "charger_voltage_output_2": RegisterInfo(2310, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
    # "charger_current_output_2": RegisterInfo(2311, INT16, ELECTRIC_CURRENT_AMPERE, 10),
    # "charger_voltage_output_3": RegisterInfo(2312, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
    # "charger_current_output_3": RegisterInfo(2313, INT16, ELECTRIC_CURRENT_AMPERE, 10),
    # "charger_L1_current": RegisterInfo(2314, INT16, ELECTRIC_CURRENT_AMPERE, 10),
    # "charger_L1_power": RegisterInfo(2315, UINT16, UnitOfPower.WATT),
    # "charger_current_limit": RegisterInfo(2316, INT16, ELECTRIC_CURRENT_AMPERE, 10, entityType=SliderWriteType("AC", True)),
    # "charger_mode": RegisterInfo(register=2317, dataType=UINT16, entityType=SelectWriteType(charger_mode)),
    # "charger_state": RegisterInfo(register=2318, dataType=UINT16, entityType=TextReadEntityType(generic_charger_state)),
    # "charger_errorcode": RegisterInfo(register=2319, dataType=UINT16, entityType=TextReadEntityType(generic_charger_errorcode)),
    # "charger_relay": RegisterInfo(register=2320, dataType=UINT16, entityType=BoolReadEntityType()),
    # "charger_alarm_lowvoltage": RegisterInfo(register=2321, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
    # "charger_alarm_highvoltage": RegisterInfo(register=2322, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger))
# }

# settings_registers = {
#     "settings_ess_acpowersetpoint": RegisterInfo(register=2700, dataType=INT16, unit=UnitOfPower.WATT, entityType=SliderWriteType("AC", True)),
#     "settings_ess_maxchargepercentage": RegisterInfo(register=2701, dataType=UINT16, unit=PERCENTAGE, entityType=SliderWriteType()),
#     "settings_ess_maxdischargepercentage": RegisterInfo(register=2702, dataType=UINT16, unit=PERCENTAGE, entityType=SliderWriteType()),
#     "settings_ess_acpowersetpoint2": RegisterInfo(2703, INT16, UnitOfPower.WATT, 0.01, SliderWriteType("AC", True)), # NOTE: Duplicate register exposed by Victron 
#     "settings_ess_maxdischargepower": RegisterInfo(2704, UINT16, UnitOfPower.WATT, 0.1, SliderWriteType("DC", False), 50),
#     "settings_ess_maxchargecurrent": RegisterInfo(register=2705, dataType=INT16, unit=ELECTRIC_CURRENT_AMPERE, entityType=SliderWriteType("DC", True)),
#     "settings_ess_maxfeedinpower": RegisterInfo(2706, INT16, UnitOfPower.WATT, 0.01, SliderWriteType("AC", True)), 
#     "settings_ess_overvoltagefeedin": RegisterInfo(register=2707, dataType=INT16, entityType=SwitchWriteType()),
#     "settings_ess_preventfeedback": RegisterInfo(register=2708, dataType=INT16, entityType=SwitchWriteType()),
#     "settings_ess_feedinpowerlimit": RegisterInfo(register=2709, dataType=INT16, entityType=BoolReadEntityType()),
#     "settings_systemsetup_maxchargevoltage": RegisterInfo(2710, UINT16, ELECTRIC_POTENTIAL_VOLT, 10, SliderWriteType("DC", False), 0.1)
# }

# gps_registers = {
#     "gps_latitude": RegisterInfo(2800, INT32, "", 10000000),
#     "gps_longitude": RegisterInfo(2802, INT32, "", 10000000),
#     "gps_course": RegisterInfo(2804, UINT16, "", 100),
#     "gps_speed": RegisterInfo(2805, UINT16, UnitOfSpeed.METERS_PER_SECOND, 100),
#     "gps_fix": RegisterInfo(register=2806, dataType=UINT16, entityType=BoolReadEntityType()),
#     "gps_numberofsatellites": RegisterInfo(2807, UINT16),
#     "gps_altitude": RegisterInfo(2808, INT32, UnitOfSpeed.METERS_PER_SECOND, 10)
# }

# pvinverter_registers = {
#     "pvinverter_position": RegisterInfo(register=1026, dataType=UINT16, entityType=TextReadEntityType(generic_position)),
#     "pvinverter_L1_voltage": RegisterInfo(1027, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
#     "pvinverter_L1_current": RegisterInfo(1028, INT16, ELECTRIC_CURRENT_AMPERE, 10),
#     "pvinverter_L1_power": RegisterInfo(1029, UINT16, UnitOfPower.WATT),
#     "pvinverter_L1_energy_forward": RegisterInfo(1030, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 100),
#     # "pvinverter_L2_voltage": RegisterInfo(1031, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
#     # "pvinverter_L2_current": RegisterInfo(1032, INT16, ELECTRIC_CURRENT_AMPERE, 10),
#     # "pvinverter_L2_power": RegisterInfo(1033, UINT16, UnitOfPower.WATT),
#     # "pvinverter_L2_energy_forward": RegisterInfo(1034, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 100),
#     # "pvinverter_L3_voltage": RegisterInfo(1035, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
#     # "pvinverter_L3_current": RegisterInfo(1036, INT16, ELECTRIC_CURRENT_AMPERE, 10),
#     # "pvinverter_L3_power": RegisterInfo(1037, UINT16, UnitOfPower.WATT),
#     # "pvinverter_L3_energy_forward": RegisterInfo(1038, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 100),
#     "pvinverter_serial": RegisterInfo(1039, STRING(7)),
#     "pvinverter_L1_energy_forward_total": RegisterInfo(1046, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
#     # "pvinverter_L2_energy_forward_total": RegisterInfo(1048, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
#     # "pvinverter_L3_energy_forward_total": RegisterInfo(1050, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
#     "pvinverter_power_total": RegisterInfo(1052, INT32, UnitOfPower.KILO_WATT),
#     "pvinverter_power_max_capacity": RegisterInfo(1054, UINT32, UnitOfPower.KILO_WATT),
#     "pvinverter_powerlimit": RegisterInfo(register=1056, dataType=UINT32, unit=UnitOfPower.WATT, entityType=SliderWriteType("AC", False))
# }

# motordrive_registers = {
#     "motordrive_rpm": RegisterInfo(2048, INT16, REVOLUTIONS_PER_MINUTE),
#     "motordrive_motor_temperature": RegisterInfo(2049, INT16, UnitOfTemperature.CELSIUS, 10),
#     "motordrive_voltage": RegisterInfo(2050, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
#     "motordrive_current": RegisterInfo(2051, INT16, ELECTRIC_CURRENT_AMPERE, 10),
#     "motordrive_power": RegisterInfo(2052, INT16, UnitOfPower.WATT, 10),
#     "motordrive_controller_temperature": RegisterInfo(2053, INT16, UnitOfTemperature.CELSIUS, 10)
# }



# class inverter_mode(Enum):
#     ON = 2
#     OFF = 4
#     ECO = 5

# inverter_info_registers = {
#     "inverter_info_firmwareversion": RegisterInfo(3125, UINT16),
#     "inverter_info_mode": RegisterInfo(register=3126, dataType=UINT16, entityType=SelectWriteType(inverter_mode)),
#     "inverter_info_productid": RegisterInfo(3127, UINT16),
#     "inverter_info_state": RegisterInfo(register=3128, dataType=UINT16, entityType=TextReadEntityType(generic_charger_state)),
# }

# #PV voltage is present here due to poor register id selection by Victron
# inverter_energy_registers = {
#     "inverter_energy_invertertoacout": RegisterInfo(3130, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
#     "inverter_energy_outtoinverter": RegisterInfo(3132, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
#     "inverter_energy_solartoacout": RegisterInfo(3134, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
#     "inverter_energy_solartobattery": RegisterInfo(3136, UINT32, UnitOfEnergy.KILO_WATT_HOUR, 100),
#     "inverter_pv_voltage_single_tracker": RegisterInfo(3138, UINT16, ELECTRIC_POTENTIAL_VOLT, 10)
# }

# inverter_tracker_registers = {
#     "inverter_tracker_0_voltage": RegisterInfo(3140, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
#     "inverter_tracker_1_voltage": RegisterInfo(3141, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
#     "inverter_tracker_2_voltage": RegisterInfo(3142, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
#     "inverter_tracker_3_voltage": RegisterInfo(3143, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
# }

# inverter_tracker_statistics_registers = {
#     "inverter_tracker_0_yield_today": RegisterInfo(3148, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
#     "inverter_tracker_1_yield_today": RegisterInfo(3149, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
#     "inverter_tracker_2_yield_today": RegisterInfo(3150, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
#     "inverter_tracker_3_yield_today": RegisterInfo(3151, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
#     "inverter_tracker_0_yield_yesterday": RegisterInfo(3152, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
#     "inverter_tracker_1_yield_yesterday": RegisterInfo(3153, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
#     "inverter_tracker_2_yield_yesterday": RegisterInfo(3154, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
#     "inverter_tracker_3_yield_yesterday": RegisterInfo(3155, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
#     "inverter_tracker_0_maxpower_today": RegisterInfo(3156, UINT16, UnitOfPower.WATT),
#     "inverter_tracker_1_maxpower_today": RegisterInfo(3157, UINT16, UnitOfPower.WATT),
#     "inverter_tracker_2_maxpower_today": RegisterInfo(3158, UINT16, UnitOfPower.WATT),
#     "inverter_tracker_3_maxpower_today": RegisterInfo(3159, UINT16, UnitOfPower.WATT),    
#     "inverter_tracker_0_maxpower_yesterday": RegisterInfo(3160, UINT16, UnitOfPower.WATT),
#     "inverter_tracker_1_maxpower_yesterday": RegisterInfo(3161, UINT16, UnitOfPower.WATT),
#     "inverter_tracker_2_maxpower_yesterday": RegisterInfo(3162, UINT16, UnitOfPower.WATT),
#     "inverter_tracker_3_maxpower_yesterday": RegisterInfo(3163, UINT16, UnitOfPower.WATT),
#     "inverter_tracker_0_power": RegisterInfo(3164, UINT16, UnitOfPower.WATT),
#     "inverter_tracker_1_power": RegisterInfo(3165, UINT16, UnitOfPower.WATT),
#     "inverter_tracker_2_power": RegisterInfo(3166, UINT16, UnitOfPower.WATT),
#     "inverter_tracker_3_power": RegisterInfo(3167, UINT16, UnitOfPower.WATT),
#     "inverter_alarm_lowsoc": RegisterInfo(register=3168, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger))
# }

# settings_ess_registers = {
#     "settings_ess_batterylife_state": RegisterInfo(register=2900, dataType=UINT16, entityType=SelectWriteType(ess_batterylife_state)),
#     "settings_ess_batterylife_minimumsoc": RegisterInfo(2901, UINT16, PERCENTAGE, 10, SliderWriteType(), 5),
#     "settings_ess_mode": RegisterInfo(register=2902, dataType=UINT16, entityType=SelectWriteType(ess_mode)),
#     "settings_ess_batterylife_soclimit": RegisterInfo(2903, UINT16, PERCENTAGE, 10),
# }

# class tank_fluidtype(Enum):
#     FUEL = 0
#     FRESH_WATER = 1
#     WASTE_WATER = 2
#     LIVE_WELL = 3
#     OIL = 4
#     SEWAGE_WATER = 5
#     GASOLINE = 6
#     DIESEL = 7
#     LPG = 8
#     LNG = 9
#     HYDRAULIC_OIL = 10
#     RAW_WATER = 11

# battery_registers = {
#     "Battery power": RegisterInfo(258, INT16, UnitOfPower.WATT),
#     "Battery voltage": RegisterInfo(259, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
#     "Starter battery voltage": RegisterInfo(260, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
#     "Battery Current": RegisterInfo(261, INT16, ELECTRIC_CURRENT_AMPERE, 10),
#     "Battery temperature": RegisterInfo(262, INT16, UnitOfTemperature.CELSIUS, 10),
#     "Mid-point voltage of the battery bank": RegisterInfo(263, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
#     "Mid-point deviation of the battery bank": RegisterInfo(264, UINT16, PERCENTAGE, 100),
#     "Consumed Amphours": RegisterInfo(265, UINT16, ELECTRIC_CURRENT_AMPERE, -10),
#     "Battery State of charge": RegisterInfo(266, UINT16, PERCENTAGE, 10),
#     "Alarm": RegisterInfo(register=267, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "Low voltage alarm": RegisterInfo(register=268, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "High voltage alarm": RegisterInfo(register=269, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "Low starter-voltage alarm": RegisterInfo(register=270, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "High starter-voltage alarm": RegisterInfo(register=271, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "Low State-of-charge alarm": RegisterInfo(register=272, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "Low temperature alarm": RegisterInfo(register=273, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "High temperature alarm": RegisterInfo(register=274, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "Mid-voltage alarm": RegisterInfo(register=275, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "Low fused-voltage alarm": RegisterInfo(register=276, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "High fused-voltage alarm": RegisterInfo(register=277, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "Fuse blown alarm": RegisterInfo(register=278, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "High internal-temperature alarm": RegisterInfo(register=279, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "Relay status": RegisterInfo(register=280, dataType=UINT16, entityType=SwitchWriteType()),
#     "Deepest discharge": RegisterInfo(281, UINT16, ELECTRIC_CURRENT_AMPERE, -10),
#     "Last discharge": RegisterInfo(282, UINT16, ELECTRIC_CURRENT_AMPERE, -10),
#     "Average discharge": RegisterInfo(283, UINT16, ELECTRIC_CURRENT_AMPERE, -10),
#     "Charge cycles": RegisterInfo(284, UINT16),
#     "Full discharges": RegisterInfo(285, UINT16),
#     "Total Ah drawn": RegisterInfo(286, UINT16, ELECTRIC_CURRENT_AMPERE, -10),
#     "Minimum voltage": RegisterInfo(287, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
#     "Maximum voltage": RegisterInfo(288, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
#     "Time since last full charge": RegisterInfo(289, UINT16, TIME_SECONDS, 0.01),
#     "Automatic syncs": RegisterInfo(290, UINT16),
#     "Low voltage alarms": RegisterInfo(291, UINT16),
#     "High voltage alarms": RegisterInfo(292, UINT16),
#     "Low starter voltage alarms": RegisterInfo(293, UINT16),
#     "High starter voltage alarms": RegisterInfo(294, UINT16),
#     "Minimum starter voltage": RegisterInfo(295, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
#     "Maximum starter voltage": RegisterInfo(296, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
#     "Low fused-voltage alarms": RegisterInfo(297, UINT16),
#     "High fused-voltage alarms": RegisterInfo(298, UINT16),
#     "Minimum fused voltage": RegisterInfo(299, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
#     "Maximum fused voltage": RegisterInfo(300, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
#     "Discharged Energy": RegisterInfo(301, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
#     "Charged Energy": RegisterInfo(302, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
#     "Time to go": RegisterInfo(303, UINT16, TIME_SECONDS, 0.01),
#     "State of health": RegisterInfo(304, UINT16, PERCENTAGE, 10),
#     "Max charge voltage": RegisterInfo(305, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
#     "Min discharge voltage": RegisterInfo(306, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
#     "Max charge current": RegisterInfo(307, UINT16, ELECTRIC_CURRENT_AMPERE, 10),
#     "Max discharge current": RegisterInfo(308, UINT16, ELECTRIC_CURRENT_AMPERE, 10),
#     "Capacity": RegisterInfo(309, UINT16, ELECTRIC_CURRENT_AMPERE, 10),
#     "Diagnostics; 1st last error timestamp": RegisterInfo(310, INT32, "timestamp"),
#     "Diagnostics; 2nd last error timestamp": RegisterInfo(312, INT32, "timestamp"),
#     "Diagnostics; 3rd last error timestamp": RegisterInfo(314, INT32, "timestamp"),
#     "Diagnostics; 4th last error timestamp": RegisterInfo(316, INT32, "timestamp"),
#     "Minimum cell temperature": RegisterInfo(318, INT16, UnitOfTemperature.CELSIUS, 10),
#     "Maximum cell temperature": RegisterInfo(319, INT16, UnitOfTemperature.CELSIUS, 10),
#     "High charge current alarm": RegisterInfo(register=320, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "High discharge current alarm": RegisterInfo(register=321, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "Cell imbalance alarm": RegisterInfo(register=322, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "Internal failure alarm": RegisterInfo(register=323, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "High charge temperature alarm": RegisterInfo(register=324, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "Low charge temperature alarm": RegisterInfo(register=325, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "Low cell voltage alarm": RegisterInfo(register=326, dataType=UINT16, entityType=TextReadEntityType(generic_alarm_ledger)),
#     "Mode": RegisterInfo(register=327, dataType=UINT16, entityType=TextReadEntityType(battery_mode))

# }

# class battery_state(Enum):
#     WAIT_START_INIT = 0
#     BEFORE_BOOT_INIT = 1
#     BEFORE_BOOT_DELAY_INIT = 2
#     WAIT_BOOT_INIT = 3
#     INITIALIZING = 4
#     BATTERY_VOLTAGE_MEASURE_INIT = 5
#     BATTERY_CALCULATE_VOLTAGE_INIT = 6
#     WAIT_BUS_VOLTAGE_INIT = 7
#     WAIT_LYNX_SHUNT_INIT = 8
#     RUNNING = 9
#     ERROR = 10
#     UNUSED = 11
#     SHUTDOWN = 12
#     SLAVE_UPDATING = 13
#     STANDBY = 14
#     GOING_TO_RUN = 15
#     PRE_CHARGING = 16

# class battery_error(Enum):
#     NONE = 0
#     BATTERY_INIT_ERROR = 1
#     NO_BATTERIES_CONNECTED = 2
#     UNKNOWN_BATTERY_CONNECTED = 3
#     DIFFERENT_BATTERY_TYPE = 4
#     NUMBER_OF_BATTERIES_INCORRECT = 5
#     LYNX_SHUNT_NOT_FOUND = 6
#     BATTERY_MEASURE_ERROR = 7
#     INTERNAL_CALCULATION_ERROR = 8
#     BATTERIES_IN_SERIES_NOT_OK = 9
#     NUMBER_OF_BATTERIES_INCORRECT_DUPLICATE_1 = 10
#     HARDWARE_ERROR = 11
#     WATCHDOG_ERROR = 12
#     OVER_VOLTAGE = 13
#     UNDER_VOLTAGE = 14
#     OVER_TEMPERATURE = 15
#     UNDER_TEMPERATURE = 16
#     HARDWARE_FAULT = 17
#     STANDBY_SHUTDOWN = 18
#     PRE_CHARGE_CHARGE_ERROR = 19
#     SAFETY_CONTACTOR_CHECK_ERROR = 20
#     PRE_CHARGE_DISCHARGE_ERROR = 21
#     ADC_ERROR = 22
#     SLAVE_ERROR = 23
#     SLAVE_WARNING = 24
#     PRE_CHARGE_ERROR = 25
#     SAFETY_CONTACTOR_ERROR = 26
#     OVER_CURRENT = 27
#     SLAVE_UPDATE_FAILED = 28
#     SLAVE_UPDATE_UNAVAILABLE = 29
#     CALIBRATION_DATA_LOST = 30
#     SETTINGS_INVALID = 31
#     BMS_CABLE = 32
#     REFERENCE_FAILURE = 33
#     WRONG_SYSTEM_VOLTAGE = 34
#     PRE_CHARGE_TIMEOUT = 35


# class battery_mode(Enum):
#     OPEN = 0
#     STANDBY = 14


# battery_detail_registers = {
#     "battery_state": RegisterInfo(register=1282, dataType=UINT16, entityType=TextReadEntityType(battery_state)),
#     "battery_error": RegisterInfo(register=1283, dataType=UINT16, entityType=TextReadEntityType(battery_error)),
#     "battery_system_switch": RegisterInfo(register=1284, dataType=UINT16, entityType=BoolReadEntityType()),
#     "battery_balancing": RegisterInfo(register=1285, dataType=UINT16, entityType=BoolReadEntityType()),
#     "battery_system_numberofbatteries": RegisterInfo(1286, UINT16),
#     "battery_system_batteriesparallel": RegisterInfo(1287, UINT16),
#     "battery_system_batteriesseries": RegisterInfo(1288, UINT16),
#     "battery_system_numberofcellsperbattery": RegisterInfo(1289, UINT16),
#     "battery_system_mincellvoltage": RegisterInfo(1290, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
#     "battery_system_maxcellvoltage": RegisterInfo(1291, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
#     "battery_diagnostics_shutdownsdueerror": RegisterInfo(1292, UINT16),
#     "battery_diagnostics_lasterror_1": RegisterInfo(register=1293, dataType=UINT16, entityType=TextReadEntityType(battery_error)),
#     "battery_diagnostics_lasterror_2": RegisterInfo(register=1294, dataType=UINT16, entityType=TextReadEntityType(battery_error)),
#     "battery_diagnostics_lasterror_3": RegisterInfo(register=1295, dataType=UINT16, entityType=TextReadEntityType(battery_error)),
#     "battery_diagnostics_lasterror_4": RegisterInfo(register=1296, dataType=UINT16, entityType=TextReadEntityType(battery_error)),
#     "battery_io_allowtocharge": RegisterInfo(register=1297, dataType=UINT16, entityType=BoolReadEntityType()),
#     "battery_io_allowtodischarge": RegisterInfo(register=1298, dataType=UINT16, entityType=BoolReadEntityType()),
#     "battery_io_externalrelay": RegisterInfo(register=1299, dataType=UINT16, entityType=BoolReadEntityType()),
#     "battery_history_minimumcellvoltage": RegisterInfo(1300, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
#     "battery_history_maximumcellvoltage": RegisterInfo(1301, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
#     "battery_system_numberofmodulesoffline": RegisterInfo(1302, UINT16),
#     "battery_system_numberofmodulesonline": RegisterInfo(1303, UINT16),
#     "battery_system_numberofmodulesblockingcharge": RegisterInfo(1304, UINT16),
#     "battery_system_numberofmodulesblockingdischarge": RegisterInfo(1305, UINT16),
#     "battery_system_minvoltagecellid": RegisterInfo(1306, STRING(4)),
#     "battery_system_maxvoltagecellid": RegisterInfo(1310, STRING(4)),
#     "battery_system_mintemperaturecellid": RegisterInfo(1314, STRING(4)),
#     "battery_system_maxtemperaturecellid": RegisterInfo(1318, STRING(4))
# }

# class system_battery_state(Enum):
#     IDLE = 0
#     CHARGING = 1
#     DISCHARGING = 2

# system_battery_registers = {
#     "system_battery_voltage": RegisterInfo(840, UINT16, ELECTRIC_POTENTIAL_VOLT, 10),
#     "system_battery_current": RegisterInfo(841, INT16, ELECTRIC_CURRENT_AMPERE, 10),
#     "system_battery_power": RegisterInfo(842, INT16, UnitOfPower.WATT),
#     "system_battery_soc": RegisterInfo(843, UINT16, PERCENTAGE),
#     "system_battery_state": RegisterInfo(register=844, dataType=UINT16, entityType=TextReadEntityType(system_battery_state)),
#     "system_battery_amphours": RegisterInfo(845, UINT16, ELECTRIC_CURRENT_AMPERE, -10), #  NOTE should be amp hours
#     "system_battery_time_to_go": RegisterInfo(846, UINT16, TIME_SECONDS, 0.01)
# }


# class digitalinput_state(Enum):
#     LOW = 0
#     HIGH = 1
#     OFF = 2
#     ON = 3
#     NO = 4
#     YES = 5
#     OPEN = 6
#     CLOSED = 7
#     ALARM = 8
#     OK = 9
#     RUNNING = 10
#     STOPPED = 11

# class digitalinput_type(Enum):
#     DOOR = 2
#     BILGE_PUMP = 3
#     BILGE_ALARM = 4
#     BURGLAR_ALARM = 5
#     SMOKE_ALARM = 6
#     FIRE_ALARM = 7
#     CO2_ALARM = 8

# class generator_runningbyconditioncode(Enum):
#     STOPPED = 0
#     MANUAL = 1
#     TEST_RUN = 2
#     LOSS_OF_COMMS = 3
#     SOC = 4
#     AC_LOAD = 5
#     BATTERY_CURRENT = 6
#     BATTERY_VOLTAGE = 7
#     INVERTER_TEMPERATURE = 8
#     INVERTER_OVERLOAD = 9
#     STOP_ON_AC1 = 10

# class generator_state(Enum):
#     STOPPED = 0
#     RUNNING = 1
#     ERROR = 10

# class generator_error(Enum):
#     NONE = 0
#     REMOTE_DISABLED = 1
#     REMOTE_FAULT = 2

# class evcharger_mode(Enum):
#     AC_INPUT_1 = 0
#     AC_OUTPUT = 1
#     AC_INPUT_2 = 2

# class evcharger_status(Enum):
#     DISCONNECTED = 0
#     CONNECTED = 1
#     CHARGING = 2
#     CHARGED = 3
#     WAITING_FOR_SUN = 4
#     WAITING_FOR_RFID = 5
#     WAITING_FOR_START = 6
#     LOW_SOC = 7
#     GROUND_FAULT = 8
#     WELDED_CONTACTS = 9
#     CP_INPUT_SHORTED = 10
#     RESIDUAL_CURRENT_DETECTED = 11
#     UNDER_VOLTAGE_DETECTED = 12
#     OVERVOLTAGE_DETECTED = 13
#     OVERHEATING_DETECTED = 14

# class alternator_state(Enum):
#     OFF = 0
#     FAULT = 2
#     BULK = 3
#     ABSORPTION = 4
#     FLOAT = 5
#     STORAGE = 6
#     EQUALIZE = 7
#     EXTERNAL_CONTROL = 252

# class alternator_errorcode(Enum):
#     HIGH_BATTERY_TEMPERATURE = 12
#     HIGH_BATTERY_VOLTAGE = 13
#     LOW_BATTERY_VOLTAGE = 14
#     VBAT_EXCEEDS_CPB = 15
#     HIGH_ALTERNATOR_TEMPERATURE = 21
#     ALTERNATOR_OVERSPEED = 22
#     INTERNAL_ERROR = 24
#     HIGH_FIELD_FET_TEMPERATURE  = 41
#     SENSOR_MISSING = 42
#     LOW_VALT = 43
#     HIGH_VOLTAGE_OFFSET = 44
#     VALT_EXCEEDS_CPB = 45
#     BATTERY_DISCONNECT_REQUEST = 51
#     BATTERY_DISCONNECT_REQUEST_DUPLICATE_1 = 52
#     BATTERY_INSTANCE_OUT_OF_RANGE = 53
#     TOO_MANY_BMSES = 54
#     AEBUS_FAULT = 55
#     TOO_MANY_Victron_DEVICES = 56
#     BATTERY_REQUESTED_DISCONNECTION = 58
#     BATTERY_REQUESTED_DISCONNECTION_DUPLICATE_1 = 59
#     BATTERY_REQUESTED_DISCONNECTION_DUPLICATE_2 = 60
#     BATTERY_REQUESTED_DISCONNECTION_DUPLICATE_3 = 61
#     BMS_LOST = 91
#     FORCED_IDLE = 92
#     DCDC_CONVERTER_FAIL = 201
#     DCDC_ERROR = 202
#     DCDC_ERROR_DUPLICATE_1 = 203
#     DCDC_ERROR_DUPLICATE_2 = 204
#     DCDC_ERROR_DUPLICATE_3 = 205
#     DCDC_ERROR_DUPLICATE_4 = 206
#     DCDC_ERROR_DUPLICATE_5 = 207

# class multi_mode(Enum):
#     CHARGER = 1
#     INVERTER = 2
#     ON = 3
#     OFF = 4

# class multi_input_type(Enum):
#     UNUSED = 0
#     GRID = 1
#     GENSET = 2
#     SHORE = 3


# solarcharger_tracker_voltage_registers = {
#     "solarcharger_tracker_0_voltage": RegisterInfo(3700, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
#     "solarcharger_tracker_1_voltage": RegisterInfo(3701, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
#     "solarcharger_tracker_2_voltage": RegisterInfo(3702, UINT16, ELECTRIC_POTENTIAL_VOLT, 100),
#     "solarcharger_tracker_3_voltage": RegisterInfo(3703, UINT16, ELECTRIC_POTENTIAL_VOLT, 100)
# }

# solarcharger_tracker_registers = {
#     "solarcharger_tracker_0_yield_today": RegisterInfo(3708, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
#     "solarcharger_tracker_1_yield_today": RegisterInfo(3709, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
#     "solarcharger_tracker_2_yield_today": RegisterInfo(3710, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
#     "solarcharger_tracker_3_yield_today": RegisterInfo(3711, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
#     "solarcharger_tracker_0_yield_yesterday": RegisterInfo(3712, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
#     "solarcharger_tracker_1_yield_yesterday": RegisterInfo(3713, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
#     "solarcharger_tracker_2_yield_yesterday": RegisterInfo(3714, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
#     "solarcharger_tracker_3_yield_yesterday": RegisterInfo(3715, UINT16, UnitOfEnergy.KILO_WATT_HOUR, 10),
#     "solarcharger_tracker_0_maxpower_today": RegisterInfo(3716, UINT16, UnitOfPower.WATT),
#     "solarcharger_tracker_1_maxpower_today": RegisterInfo(3717, UINT16, UnitOfPower.WATT),
#     "solarcharger_tracker_2_maxpower_today": RegisterInfo(3718, UINT16, UnitOfPower.WATT),
#     "solarcharger_tracker_3_maxpower_today": RegisterInfo(3719, UINT16, UnitOfPower.WATT),
#     "solarcharger_tracker_0_maxpower_yesterday": RegisterInfo(3720, UINT16, UnitOfPower.WATT),
#     "solarcharger_tracker_1_maxpower_yesterday": RegisterInfo(3721, UINT16, UnitOfPower.WATT),
#     "solarcharger_tracker_2_maxpower_yesterday": RegisterInfo(3722, UINT16, UnitOfPower.WATT),
#     "solarcharger_tracker_3_maxpower_yesterday": RegisterInfo(3723, UINT16, UnitOfPower.WATT),
#     "solarcharger_tracker_0_pv_power": RegisterInfo(3724, UINT16, UnitOfPower.WATT),
#     "solarcharger_tracker_1_pv_power": RegisterInfo(3725, UINT16, UnitOfPower.WATT),
#     "solarcharger_tracker_2_pv_power": RegisterInfo(3726, UINT16, UnitOfPower.WATT),
#     "solarcharger_tracker_3_pv_power": RegisterInfo(3727, UINT16, UnitOfPower.WATT),    
# }

# class genset_status(Enum):
#     STANDBY = 0
#     STARTUP_1 = 1
#     STARTUP_2 = 2
#     STARTUP_3 = 3
#     STARTUP_4 = 4
#     STARTUP_5 = 5
#     STARTUP_6 = 6
#     STARTUP_7 = 7
#     RUNNING = 8
#     STOPPING = 9
#     ERROR = 10

# class genset_errorcode(Enum):
#     NONE = 0
#     AC_L1_VOLTAGE_TOO_LOW = 1
#     AC_L1_FREQUENCY_TOO_LOW = 2
#     AC_L1_CURRENT_TOO_LOW = 3
#     AC_L1_POWER_TOO_LOW = 4
#     EMERGENCY_STOP = 5
#     SERVO_CURRENT_TOO_LOW = 6
#     OIL_PRESSURE_TOO_LOW = 7
#     ENGINE_TEMPERATURE_TOO_LOW = 8
#     WINDING_TEMPERATURE_TOO_LOW = 9
#     EXHAUST_TEMPERATURE_TOO_LOW = 10
#     STARTER_CURRENT_TOO_LOW = 13
#     GLOW_CURRENT_TOO_LOW = 14
#     GLOW_CURRENT_TOO_LOW_DUPLICATE_1 = 15
#     FUEL_HOLDING_MAGNET_CURRENT_TOO_LOW = 16
#     STOP_SOLENOID_HOLD_COIL_CURRENT_TOO_LOW = 17
#     STOP_SOLENOID_PULL_COIL_CURRENT_TOO_LOW = 18
#     OPTIONAL_DC_OUT_CURRENT_TOO_LOW = 19
#     OUTPUT_5V_VOLTAGE_TOO_LOW = 20
#     BOOST_OUTPUT_CURRENT_TOO_LOW = 21
#     PANEL_SUPPLY_CURRENT_TOO_HIGH = 22
#     STARTER_BATTERY_VOLTAGE_TOO_LOW = 25
#     ROTATION_TOO_LOW_STARTUP_ABORTED = 26
#     ROTATION_TOO_LOW = 28
#     POWER_CONTACTER_CURRENT_TOO_LOW = 29
#     AC_L2_VOLTAGE_TOO_LOW = 30
#     AC_L2_FREQUENCY_TOO_LOW = 31
#     AC_L2_CURRENT_TOO_LOW = 32
#     AC_L2_POWER_TOO_LOW = 33
#     AC_L3_VOLTAGE_TOO_LOW = 34
#     AC_L3_FREQUENCY_TOO_LOW = 35
#     AC_L3_CURRENT_TOO_LOW = 36
#     AC_L3_POWER_TOO_LOW = 37
#     FUEL_TEMPERATURE_TOO_LOW = 62
#     FUEL_LEVEL_TOO_LOW = 63
#     AC_L1_VOLTAGE_TOO_HIGH = 65
#     AC_L1_FREQUENCY_TOO_HIGH = 66
#     AC_L1_CURRENT_TOO_HIGH = 67
#     AC_L1_POWER_TOO_HIGH = 68
#     SERVO_CURRENT_TOO_HIGH = 70
#     OIL_PRESSURE_TOO_HIGH = 71
#     ENGINE_TEMPERATURE_TOO_HIGH = 72
#     WINDING_TEMPERATURE_TOO_HIGH = 73
#     EXHAUST_TEMPERATURE_TOO_HIGH = 74 #NOTE modbustcp spec says it should be too low but that is already specified in the low grouping therefore assuming this state is used for HIGH temp
#     STARTER_CURRENT_TOO_HIGH = 77 #NOTE same as 74 applies here
#     GLOW_CURRENT_TOO_HIGH = 78
#     GLOW_CURRENT_TOO_HIGH_DUPLICATE_1 = 79
#     FUEL_HOLDING_MAGNET_CURRENT_TOO_HIGH = 80
#     STOP_SOLENOID_HOLD_COIL_CURRENT_TOO_HIGH = 81
#     STOP_SOLENOID_PULL_COIL_CURRENT_TOO_HIGH = 82
#     OPTIONAL_DC_OUT_CURRENT_TOO_HIGH  = 83
#     OUTPUT_5V_TOO_HIGH = 84
#     BOOST_OUTPUT_CURRENT_TOO_HIGH = 85
#     STARTER_BATTERY_VOLTAGE_TOO_HIGH = 89
#     ROTATION_TOO_HIGH_STARTUP_ABORTED = 90
#     ROTATION_TOO_HIGH = 92
#     POWER_CONTACTER_CURRENT_TOO_HIGH  = 93
#     AC_L2_VOLTAGE_TOO_HIGH = 94
#     AC_L2_FREQUENCY_TOO_HIGH = 95
#     AC_L2_CURRENT_TOO_HIGH = 96
#     AC_L2_POWER_TOO_HIGH = 97
#     AC_L3_VOLTAGE_TOO_HIGH = 98
#     AC_L3_FREQUENCY_TOO_HIGH = 99
#     AC_L3_CURRENT_TOO_HIGH = 100
#     AC_L3_POWER_TOO_HIGH = 101
#     FUEL_TEMPERATURE_TOO_HIGH = 126
#     FUEL_LEVEL_TOO_HIGH = 127
#     LOST_CONTROL_UNIT = 130
#     LOST_PANEL = 131
#     SERVICE_NEEDED = 132
#     LOST_THREE_PHASE_MODULE = 133
#     LOST_AGT_MODULE = 134
#     SYNCHRONIZATION_FAILURE = 135
#     INTAKE_A154
#     INVERTER_OVER_TEMPERATURE = 155
#     INVERTER_OVERLOAD = 156
#     INVERTER_COMMMUNICATION_LOST  = 157
#     INVERTER_SYNC_FAILED = 158
#     CAN_COMMUNICATION_LOST = 159
#     L1_OVERLOAD = 160
#     L2_OVERLOAD = 161
#     L3_OVERLOAD = 162
#     DC_OVERLOAD = 163
#     DC_OVERVOLTAGE = 164
#     EMERGENCY_STOP_DUPLICATE_1 = 165
#     NO_CONNECTION = 166


# class temperature_type(Enum):
#     BATTERY = 0
#     FRIDGE = 1
#     GENERIC = 2IRFILTER = 137
#     LOST_SYNC_MODULE = 139
#     LOAD_BALANCE_FAILED = 140
#     SYNC_MODE_DEACTIVATED  = 141
#     ENGINE_CONTROLLER = 142
#     ROTATING_FIELD_WRONG = 148
#     FUEL_LEVEL_SENSOR_LOST = 149
#     INIT_FAILED = 150
#     WATCHDOG = 151
#     OUTAGE_WINDING = 152
#     OUTAGE_EXHAUST = 153
#     OUTAGE_CYCLE_HEAD = 


# class generic_position(Enum):
#     AC_INPUT_1 = 0
#     AC_OUTPUT = 1
#     AC_INPUT_2 = 2

# class ess_batterylife_state(Enum):
#     BL_DISABLED_DUPLICATE_1 = 0
#     RESTARTING = 1
#     SELF_CONSUMPTION = 2
#     SELF_CONSUMPTION_DUPLICATE_1 = 3
#     SELF_CONSUMPTION_DUPLICATE_2 = 4
#     DISCHARGE_DISABLED = 5
#     FORCE_CHARGE = 6
#     SUSTAIN = 7
#     LOW_SOC_RECHARGE = 8
#     KEEP_BATTERIES_CHARGED = 9
#     BL_DISABLED = 10
#     BL_DISABLED_LOW_SOC = 11
#     BL_DISABLED_LOC_SOC_RECHARGE = 12

