import logging
import threading

from flask import Flask

from modem import automateModem
from speaker import turnOnSpeaker

app = Flask(__name__)


@app.route('/turn-on-speaker', methods=['GET'])
def turn_on_speaker():
    turnOnSpeaker()
    return 'Speaker turned on'


@app.route('/automate-modem', methods=['GET'])
def automate_modem():
    automateModem()
    return 'Automate modem ran successfully'


@app.route('/', methods=['GET'])
def main():
    return 'Hello Dhanu!'


if __name__ == '__main__':
    # Start the background task in a separate thread
    app.run()
