"""DataUpdateCoordinator for Bobcat Machine IQ."""
from __future__ import annotations

from datetime import timedelta

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

# TODO: Implement data coordinator for AEMP API polling


class BobcatMachineIQCoordinator(DataUpdateCoordinator):
    """Class to manage fetching Bobcat Machine IQ data from AEMP API."""

    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize."""
        super().__init__(
            hass,
            logger=None,  # TODO: Add logger
            name="Bobcat Machine IQ",
            update_interval=timedelta(minutes=5),
        )

    async def _async_update_data(self) -> dict:
        """Fetch data from AEMP API."""
        # TODO: Implement API data fetching
        return {}
