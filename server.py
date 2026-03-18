import os
import uuid
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from livekit import api
from livekit.api import LiveKitAPI, ListRoomsRequest

import asyncio

# Load environment variables
load_dotenv()

LIVEKIT_URL = os.getenv("LIVEKIT_URL")
API_KEY = os.getenv("LIVEKIT_API_KEY")
API_SECRET = os.getenv("LIVEKIT_API_SECRET")

# Flask app setup
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Utility to list room names
async def get_rooms():
    client = LiveKitAPI(api_key=API_KEY, api_secret=API_SECRET, host=LIVEKIT_URL)
    res = await client.room.list_rooms(ListRoomsRequest())
    await client.aclose()
    return [room.name for room in res.rooms]

# Generate unique room name
async def generate_room_name():
    name = "room-" + str(uuid.uuid4())[:8]
    rooms = await get_rooms()
    while name in rooms:
        name = "room-" + str(uuid.uuid4())[:8]
    return name

# Serve the frontend UI
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Flask route (sync) for token generation
@app.route("/getToken", methods=["GET"])
def get_token():
    name = request.args.get("name", "guest")
    room = request.args.get("room")

    async def generate():
        nonlocal room
        if not room:
            room = await generate_room_name()

        token = api.AccessToken(API_KEY, API_SECRET) \
            .with_identity(name) \
            .with_name(name) \
            .with_grants(api.VideoGrants(
                room_join=True,
                room=room
            ))
        return token.to_jwt(), room

    token_jwt, room = asyncio.run(generate())
    return jsonify({
        "token": token_jwt,
        "room": room,
        "identity": name,
        "livekitUrl": LIVEKIT_URL,
    })

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
