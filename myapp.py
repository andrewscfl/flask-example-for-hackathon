import json
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/h')
def hello_world():
    return "Hello world"

@app.route('/json')
def returns_json():
    #do a bunch of calulations or db retrival here
    return {
        "tookdogout" : 1,
        "username" : "andrewaccount"
    }

@app.route('/rd', methods=['POST'])
@cross_origin()
def reciveing_data():
    return jsonify(request.json)


