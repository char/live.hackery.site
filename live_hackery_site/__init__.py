from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "live.hackery.site is a private screen sharing service."

from .rtmp_callback import *
# from .viewer import *
