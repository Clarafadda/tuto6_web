import os

import redis
from flask import Flask, jsonify

app = Flask(__name__)
db = redis.Redis(host=os.environ["DB_HOST"])


@app.get("/visits")
def visits():
    return jsonify(visits=db.incr("visits"))