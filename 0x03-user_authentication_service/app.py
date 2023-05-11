#!/usr/bin/env python3
""" Creating flask app module """

from flask import Flask, jsonify


app = Flask(__name__)  # Flask app instance created


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """ GET /
    Return a welcome message
    """
    return jsonify({"message": "Bienvenue"})  # jsonify converts dict to JSON


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
