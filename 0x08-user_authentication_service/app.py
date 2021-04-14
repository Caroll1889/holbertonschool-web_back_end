#!/usr/bin/env python3
"""Set up a basic Flask app.
"""

from flask import Flask, jsonify, request, abort, redirect
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


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """Log out"""
    session = request.cookies.get('session_id')

    if session:
        user = AUTH.get_user_from_session_id(session_id=session)
        if user:
            AUTH.destroy_session(user.id)
            return redirect('/')
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
