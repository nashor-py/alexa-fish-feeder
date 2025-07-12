from flask import Flask, request, jsonify, make_response
import requests

app = Flask(__name__)
FIREBASE_URL = "https://fish-feeder-1670f-default-rtdb.firebaseio.com/feed_now.json"

@app.route("/", methods=["POST"])
def alexa_webhook():
    try:
        req = request.get_json()

        intent_name = req.get("request", {}).get("intent", {}).get("name", "")
        if intent_name == "FeedNowIntent":
            # Trigger feeding
            requests.put(FIREBASE_URL, json=True)

            response_data = {
                "version": "1.0",
                "response": {
                    "outputSpeech": {
                        "type": "PlainText",
                        "text": "Feeding your fish now!"
                    },
                    "shouldEndSession": True
                }
            }
            return make_response(jsonify(response_data), 200)

        else:
            response_data = {
                "version": "1.0",
                "response": {
                    "outputSpeech": {
                        "type": "PlainText",
                        "text": "I didn't understand that command."
                    },
                    "shouldEndSession": True
                }
            }
            return make_response(jsonify(response_data), 200)

    except Exception as e:
        print("Error:", e)
        error_response = {
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "There was an error triggering the feeder."
                },
                "shouldEndSession": True
            }
        }
        return make_response(jsonify(error_response), 200)
