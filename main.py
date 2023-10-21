import time

from device import turnOff, turnOn, getStatus
from modem import getBatteryPercent

while True:
    battery = getBatteryPercent()
    if battery > 80 and getStatus():
        turnOff()
    if battery < 20 and not getStatus():
        turnOn()

    # Wait for 60 seconds (1 minute) before running the task again
    time.sleep(60)
