import json
import logging
import subprocess
import time

import requests
import xmltodict

from device import getStatus, turnOff, turnOn

IWGETID_PATH = '/usr/sbin/iwgetid'


def getBatteryPercent():
    try:
        url = "http://192.168.1.1/mark_title.w.xml"

        payload = {}
        headers = {
            'Referer': 'http://192.168.1.1/index.html'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        # Parse the XML data to a Python dictionary
        xml_dict = xmltodict.parse(response.text)

        # Convert the dictionary to JSON
        json_data = json.dumps(xml_dict, indent=4)

        data_dict = json.loads(json_data)
        return int(data_dict['title']['batt_p'])
    except:
        return None


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


def automateModem():
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
