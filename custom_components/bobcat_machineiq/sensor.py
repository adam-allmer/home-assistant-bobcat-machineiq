"""Sensor platform for Bobcat Machine IQ."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

# TODO: Implement sensor entities for fuel, location, engine status, etc.
# API Reference: https://developer.bobcat.com/


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Bobcat Machine IQ sensor entities."""
    # TODO: Create sensor entities
    pass
