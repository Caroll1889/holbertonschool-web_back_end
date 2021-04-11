#!/usr/bin/env python3
"""Set up a basic Flask app.
"""

from flask import Flask, jsonify


@app.route('/', methods=['GET'])
def index() -> str:
    """Basic Flask app"""
    return jsonify({"message": "Bienvenue"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
