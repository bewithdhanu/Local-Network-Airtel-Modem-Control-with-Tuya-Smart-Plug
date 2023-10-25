from flask import Flask

from modem import automateModem
from speaker import turnOnSpeaker

app = Flask(__name__)


@app.route('/turn-on-speaker', methods=['GET'])
def turn_on_speaker():
    turnOnSpeaker()
    return 'Speaker turned on'


if __name__ == '__main__':
    automateModem()
    app.run()
