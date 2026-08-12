"""Sensor platform for APsystems Connect."""

from homeassistant.components.sensor import SensorDeviceClass, SensorEntity
from homeassistant.const import UnitOfPower
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .coordinator import APsystemsDataCoordinator


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up APsystems Connect sensors."""

    coordinator = entry.runtime_data

    async_add_entities(
        [
            APsystemsCurrentPowerSensor(coordinator),
        ]
    )


class APsystemsCurrentPowerSensor(CoordinatorEntity, SensorEntity):
    """Current Power sensor for APsystems Connect."""

    _attr_name = "Current Power"
    _attr_device_class = SensorDeviceClass.POWER
    _attr_native_unit_of_measurement = UnitOfPower.WATT

    def __init__(self, coordinator: APsystemsDataCoordinator):
        """Initialiseer de Current Power sensor."""

        super().__init__(coordinator)

    @property
    def native_value(self):
        """Geef het actuele vermogen terug."""

        return self.coordinator.data["current_power"]