import os, sys, time

from flask import Flask, redirect, url_for, request, render_template, session
from pymongo import MongoClient


import os

PORT = int(os.getenv('VCAP_APP_PORT', '8000'))

global humidity, temperature

app = Flask(__name__)
app.secret_key = "123213"


@app.route('/jsondata', methods=['POST', 'GET'])
def welcome():
    client = MongoClient("mongodb://iot:iot@ds119049.mlab.com:19049/iot")
    db = client.iot
    #json = request.get_json()
    temperature = request.values['temp']
    humidity = request.values['humid']
    #print json

    db.thermostat.insert_one(
        {
            "temperature": temperature,
            "humidity": humidity
        }
    )

    return 12

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)