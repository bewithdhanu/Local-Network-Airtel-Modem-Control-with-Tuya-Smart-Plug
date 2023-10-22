import logging
import time
import os
import subprocess

from device import turnOff, turnOn, getStatus
from modem import getBatteryPercent

IWGETID_PATH = '/usr/sbin/iwgetid'


def is_wifi_connected():
    try:
        # Use the 'iwgetid' command to check if the system is connected to Wi-Fi
        subprocess.check_output([IWGETID_PATH])
        return True
    except subprocess.CalledProcessError:
        return False


def wait_for_wifi_connection(timeout=300):
    start_time = time.time()
    while not is_wifi_connected():
        if time.time() - start_time >= timeout:
            logging.info("Timeout reached. Wi-Fi not connected.")
            break
        time.sleep(1)


wait_for_wifi_connection()
logging.info("Wi-Fi is connected!")
while True:
    battery = getBatteryPercent()
    logging.info('battery: ' + str(battery))
    if battery is not None:
        if battery > 80 and getStatus():
            turnOff()
        if battery < 20 and not getStatus():
            turnOn()
    # Wait for 60 seconds (1 minute) before running the task again
    time.sleep(60)
