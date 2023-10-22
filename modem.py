import json

import requests
import xmltodict


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
