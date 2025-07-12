@app.route("/", methods=["POST"])
def alexa_webhook():
    req = request.get_json()
    intent_name = req["request"]["intent"]["name"]

    if intent_name == "FeedNowIntent":
        try:
            requests.put(FIREBASE_URL, json=True)
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
        except:
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
