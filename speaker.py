from env import ENDPOINT, ACCESS_ID, ACCESS_KEY, USERNAME, PASSWORD

from tuya_iot import TuyaOpenAPI, TUYA_LOGGER
import logging

# Initialization of tuya openapi
openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect(USERNAME, PASSWORD, "91", 'smartlife')

# # Uncomment the following lines to see logs.

TUYA_LOGGER.setLevel(logging.DEBUG)

DEVICE_ID = 'd713aeeaad2a788346rser'


def turnOnSpeaker():
    commands = {'commands': [{"code": "switch", "value": True}]}
    openapi.post('/v1.0/devices/{}/commands'.format(DEVICE_ID), commands)
