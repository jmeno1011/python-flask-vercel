from flask import Flask
from flask_cors import CORS

import src

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/home')
def home():
    return 'home!'


@app.route('/date')
def now():
    time = src.timeNow()
    return time


if __name__ == '__main__':
    app.run()
