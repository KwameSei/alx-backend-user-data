#!/usr/bin/env python3
""""
 Handling all routes for Session Authentication
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv
from api.v1.app import auth


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login route
    Return:
      - JSON User object
    """
    email = request.form.get('email')  # get email from request
    if not email:
        return jsonify({"error": "email missing"}), 400  # if no email
    password = request.form.get('password')  # get password from request
    if not password:
        return jsonify({"error": "password missing"}), 400
    try:   # search for user by email
        all_users = User.search({'email': email})
    except Exception:  # if no user found
        return jsonify({"error": "no user found for this email"}), 404

    if not all_users:  # if no user found
        return jsonify({"error": "no user found for this email"}), 404

    for user in all_users:   # check if password matches
        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401

        session_id = auth.create_session(user.id)  # create session_id
        cookie = getenv('SESSION_NAME')  # get cookie name

        response = jsonify(user.to_json())  # jsonify user
        response.set_cookie(cookie, session_id)  # set cookie
        return response

    return jsonify({"error": "no user found for this email"}), 404
