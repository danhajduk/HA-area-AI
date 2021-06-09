DOMAIN = "ha_area_ai"


async def async_setup(hass, config):
    hass.states.async_set("ha_area_ai.world", "Paulus")

    # Return boolean to indicate that initialization was successful.
    return True
