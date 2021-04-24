#!/usr/bin/env python3
"""
Get locale from request
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict
from pytz import timezone

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Configuration class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route('/', methods=['GET'], strict_slashes=False)
def config():
    """
    Welcome page
    """
    return render_template("7-index.html")


def get_user() -> Dict:
    """Function that returns a user dictionary"""
    try:
        return users.get(int(request.args.get('login_as')))
    except Exception:
        return None


@app.before_request
def before_request():
    """Find a user if any"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Function that determines the best match with
    the supported languages.
    """
    if request.args.get("locale"):
        return request.args.get("locale")
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Infer appropriate time zone
    """
    tz = request.args.get('timezone')

    if tz:
        try:
            return pytz.timezone(tz)
        except UnknownTimeZoneError:
            return None
    if g.user:
        tzone = g.user.get('timezone')
        try:
            return pytz.timezone(tzone)
        except UnknownTimeZoneError:
            return None
    return pytz.timezone('utc')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
