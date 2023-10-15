
# Local Network Airtel Modem Control with Tuya Smart Plug

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

## Overview

This project allows you to control your Airtel modem using a Tuya Smart Plug over your local network. With this solution, you can conveniently power cycle your modem remotely, improving its stability and connectivity without the need to physically unplug and plug it in.

## Features

- **Remote Modem Control**: Control your Airtel modem remotely via a Tuya Smart Plug.
- **Improved Connectivity**: Easily power cycle the modem for enhanced stability and performance.
- **Automation**: Integrate this solution into your home automation setup.
- **Security**: Operates within your local network, ensuring the security of your data.

## Prerequisites

Before you get started, ensure you have the following:

- A Tuya Smart (SmartLife) Plug device & Tuya IoT Platform account
- Python 3.x installed
- Airtel modem 

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/bewithdhanu/Local-Network-Airtel-Modem-Control-with-Tuya-Smart-Plug.git
   ```

2. Install the required Python packages:

   ```shell
   pip install -r requirements.txt
   ```

3. Configure your Tuya Smart Plug credentials and network settings (instructions in the project documentation).

4. Run the Python script to control your modem via the Tuya Smart Plug.

## Configuration

- Copy `env.py.example` to `env.py` using this command `cp env.py.example env.py`
	```py
	ACCESS_ID = ""  
	ACCESS_KEY = ""  
	USERNAME = ""  
	PASSWORD = ""  
	DEVICE_ID = ""  
	ENDPOINT = ""
	```
- Update all values with actual data

## Usage

Explain how to use your project once it's installed. Provide examples and code snippets if applicable.

```shell
python main.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Tuya Official Python SDK](https://github.com/tuya/tuya-iot-python-sdk)


## Authors

|Name|Type|
|--|--|
|[Dhanu K](https://github.com/bewithdhanu)|Author|