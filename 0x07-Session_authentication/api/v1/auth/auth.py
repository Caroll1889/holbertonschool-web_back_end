#!/usr/bin/env python3
"""Auth class
"""

from flask import request
from typing import List, TypeVar
import os


class Auth:
    """class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Required authentication"""
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False
        if path[-1] != '/':  # Comprobar si el path no termina en '/'
            path += '/'
        for i in excluded_paths:
            if i == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authentication header"""
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user"""
        return None

    def session_cookie(self, request=None):
        """Function that returns a cookie value from a request"""
        if request is None:
            return None
        session = os.getenv('SESSION_NAME')
        return request.cookies.get(session)
