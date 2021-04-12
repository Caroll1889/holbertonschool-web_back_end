#!/usr/bin/env python3
"""Set up a basic Flask app.
"""

from flask import Flask, jsonify, request, abort
from auth import Auth

AUTH = Auth()


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """Basic Flask app"""
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """End-point to register a user."""
    email = request.form.get('email')
    passwd = request.form.get('password')

    try:
        AUTH.register_user(email, passwd)
        return jsonify({f"email": email, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """Log in"""

    email = request.form.get('email')
    passwd = request.form.get('password')

    if not AUTH.valid_login(email, passwd):
        abort(401)
    new_id = AUTH.create_session(email)
    res = jsonify({"email": email, "message": "logged in"})
    res.set_cookie('session_id', new_id)
    return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
