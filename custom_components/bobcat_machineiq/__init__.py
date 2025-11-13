"""The Bobcat Machine IQ integration."""
from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

# TODO: Implement integration initialization
DOMAIN = "bobcat_machineiq"


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Bobcat Machine IQ from a config entry."""
    # TODO: Implement setup logic
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    # TODO: Implement unload logic
    return True
