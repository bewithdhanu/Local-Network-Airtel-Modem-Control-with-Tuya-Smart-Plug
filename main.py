import time

from device import turnOff, turnOn
from modem import getBatteryPercent

while True:
    battery = getBatteryPercent()
    if battery > 80:
        turnOff()
    if battery < 20:
        turnOn()

    # Wait for 60 seconds (1 minute) before running the task again
    time.sleep(60)
