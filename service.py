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


@app.route('/', methods=['GET'])
def main():
    return 'Hello Dhanu!'


if __name__ == '__main__':
    # Start the background task in a separate thread
    try:
        task_thread = threading.Thread(target=automateModem)
        task_thread.start()
    except:
        logging.error("automateModem has failed to start")
    finally:
        app.run()
