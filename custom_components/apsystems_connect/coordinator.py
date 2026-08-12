"""Data coordinator for APsystems Connect."""

from datetime import timedelta
import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)

from apsystems_connect_core.local_api import get_ecu_info

from .const import DOMAIN


_LOGGER = logging.getLogger(__name__)


class APsystemsDataCoordinator(DataUpdateCoordinator):
    """Coordinator voor APsystems ECU-data."""

    def __init__(self, hass: HomeAssistant):
        """Initialiseer de APsystems data coordinator."""

        super().__init__(
            hass,
            logger=_LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=30),
        )

    async def _async_update_data(self):
        """Haal nieuwe gegevens op van de APsystems ECU."""

        try:
            return await self.hass.async_add_executor_job(get_ecu_info)

        except Exception as err:
            raise UpdateFailed(
                f"Kan geen gegevens ophalen van de APsystems ECU: {err}"
            ) from err