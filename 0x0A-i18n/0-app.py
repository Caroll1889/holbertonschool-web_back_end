#!/usr/bin/env python3
"""Basic Flask app
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['POST'], strict_slashes=False)
def index():
    """
    Welcome page
    """
    return render_template('0-index.html')
