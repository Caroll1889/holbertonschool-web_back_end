#!/usr/bin/env python3
"""Auth class
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Required authentication"""
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/': # Comprobar si el path termina en '/'
            path += '/'
        for i in excluded_paths:
            if i == path:
                return False
            

    def authorization_header(self, request=None) -> str:
        """"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """"""
        return None
