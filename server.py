import os
import uuid
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from livekit import api
from livekit.api import LiveKitAPI, ListRoomsRequest

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

# Flask route (async) for token generation — avoids creating/destroying a new
# asyncio event loop on every request, which is the overhead of asyncio.run().
@app.route("/getToken", methods=["GET"])
async def get_token():
    name = request.args.get("name", "guest")
    room = request.args.get("room")

    if not room:
        room = await generate_room_name()

    token = api.AccessToken(API_KEY, API_SECRET) \
        .with_identity(name) \
        .with_name(name) \
        .with_grants(api.VideoGrants(
            room_join=True,
            room=room
        ))
    token_jwt = token.to_jwt()
    return jsonify({"token": token_jwt, "room": room, "identity": name})

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
