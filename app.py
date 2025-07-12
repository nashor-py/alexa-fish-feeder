from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

FIREBASE_URL = 'https://fish-feeder-1670f-default-rtdb.firebaseio.com/feed_now.json'

@app.route('/feed', methods=['POST'])
def feed():
    print("Received Alexa trigger")
    requests.put(FIREBASE_URL, json=True)
    return jsonify({'message': 'Feeding triggered'}), 200

@app.route('/', methods=['GET'])
def index():
    return "Fish Feeder Python Backend is running!"