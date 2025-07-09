from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
CORS(app)

#  Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client["webhookdb"]  # use lowercase to match existing DB
events_collection = db["events"]

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Webhook received:", data)

    # Extract necessary fields
    event = {
        "author": data.get("author", "Unknown"),
        "actionType": data.get("actionType", "Unknown"),
        "fromBranch": data.get("fromBranch", "dev"),
        "toBranch": data.get("toBranch", "main"),
        "timestamp": datetime.utcnow()  # Note: this gives UTC time
    }

    # Insert into MongoDB
    events_collection.insert_one(event)
    return jsonify({"message": "Event received and stored"}), 200

@app.route("/events", methods=["GET"])
def get_events():
    events = list(events_collection.find({}, {"_id": 0}))
    return jsonify(events), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
