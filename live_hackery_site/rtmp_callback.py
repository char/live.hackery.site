from live_hackery_site import app
from flask import request
import json

auth = {}
with f as open("auth.json"):
    auth = json.load(f)

@app.route("/callback", methods=["GET"])
def is_valid():
    stream_name = request.args.get("name", default="nobody", type=str)
    key = request.args.get("psk", default="", type=str)

    if stream_name in auth and auth[stream_name] == key:
        return "Created", 201

    return "Unauthorized", 403

