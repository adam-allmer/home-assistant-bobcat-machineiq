"""Config flow for Bobcat Machine IQ integration."""
from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN

# TODO: Implement configuration flow for user setup


class BobcatMachineIQConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Bobcat Machine IQ."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        # TODO: Implement user configuration step
        if user_input is not None:
            return self.async_create_entry(title="Bobcat Machine IQ", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
        )
