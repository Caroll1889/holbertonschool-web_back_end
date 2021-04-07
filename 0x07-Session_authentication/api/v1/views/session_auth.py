#!/usr/bin/env python3
""" routes for the Session authentication
"""

from api.v1.views import app_views
from flask import request, abort, jsonify
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """POST /auth_session/login """
    email = request.form.get('email')
    passwd = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not passwd:
        return jsonify({"error": "password missing"}), 400

    try:
        user = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    for i in user:
        if not i.is_valid_password(passwd):
            return jsonify({"error": "wrong password"}), 401
        else:
            from api.v1.app import auth
            user_id = i.id
            session = auth.create_session(user_id)
            res = jsonify(i.to_json())
            name = os.getenv('SESSION_NAME')
            res.set_cookie(name, session)

    return res


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """Function that deletes the user session / logout"""
    from api.v1.app import auth

    delete = auth.destroy_session(request)

    if not delete:
        abort(404)
    return jsonify({}), 200
