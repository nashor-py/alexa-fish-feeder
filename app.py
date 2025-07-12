from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

FIREBASE_URL = "https://fish-feeder-1670f-default-rtdb.firebaseio.com/feed_now.json"

@app.route("/", methods=["POST"])
def alexa_webhook():
    try:
        req = request.get_json()

        intent_name = req.get("request", {}).get("intent", {}).get("name", "")
        if intent_name == "FeedNowIntent":
            # Update Firebase with feed_now = true
            requests.put(FIREBASE_URL, json=True)  # incorrect
            # Correct version:
            requests.put(FIREBASE_URL, json=True)  # ❌

            requests.put(FIREBASE_URL, json={"feed_now": True})  # ✅

            return jsonify({
                "version": "1.0",
                "response": {
                    "outputSpeech": {
                        "type": "PlainText",
                        "text": "Feeding your fish now!"
                    },
                    "shouldEndSession": True
                }
            })
        else:
            return jsonify({
                "version": "1.0",
                "response": {
                    "outputSpeech": {
                        "type": "PlainText",
                        "text": "I didn't understand that command."
                    },
                    "shouldEndSession": True
                }
            })
    except Exception as e:
        print("Error:", e)
        return jsonify({
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "There was an error triggering the feeder."
                },
                "shouldEndSession": True
            }
        })
