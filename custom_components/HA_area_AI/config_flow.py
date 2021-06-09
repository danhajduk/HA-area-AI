from homeassistant import config_entries
from .const import DOMAIN


class ExampleConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Example config flow."""
    await self.async_set_unique_id(device_unique_id)
    self._abort_if_unique_id_configured()

