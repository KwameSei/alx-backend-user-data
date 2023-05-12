#!/usr/bin/env python3
""" Creating flask app module """

from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)  # Flask app instance created


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """ GET /
    Return a welcome message
    """
    return jsonify({"message": "Bienvenue"})  # jsonify converts dict to JSON

@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """ POST /users route 
    Register the user with email and password
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": "{}".format(user.email),
                      "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
