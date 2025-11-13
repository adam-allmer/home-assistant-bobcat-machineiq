# home-assistant-bobcat-machineiq
Home Assistant integration for Bobcat Machine IQ telematics. Pulls real-time equipment data—fuel, location, engine status—via AEMP API.

## API Reference
This integration uses the Bobcat Developer API. For API documentation, visit: https://developer.bobcat.com/

## Installation
1. Copy the `custom_components/bobcat_machineiq` folder to your Home Assistant `custom_components` directory
2. Restart Home Assistant
3. Add the integration through the Home Assistant UI

## Development
This is a work in progress. Placeholder files are currently in place for:
- Configuration flow
- Data coordinator for API polling
- Sensor entities for equipment data
