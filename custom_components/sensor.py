"""Sensor platform for APsystems Connect."""

from homeassistant.components.sensor import SensorDeviceClass, SensorEntity
from homeassistant.const import UnitOfPower

from .local_ecu import LocalECU
from .parser import parse_ecu_info