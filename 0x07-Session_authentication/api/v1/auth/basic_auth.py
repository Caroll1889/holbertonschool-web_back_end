#!/usr/bin/env python3
"""Auth class
"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """Basic auth"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Basic - Base64 part"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header.startswith('Basic '):
            return authorization_header[6:]
        else:
            return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """Basic - Base64 decode"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            base64_authorization_header = base64.b64decode(
                                          base64_authorization_header)
            return base64_authorization_header.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """Basic - User credentials"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' in decoded_base64_authorization_header:
            val = decoded_base64_authorization_header.split(sep=':')
            return tuple(val)
        else:
            return None, None

    def user_object_from_credentials(self, user_email:
                                     str, user_pwd: str) -> TypeVar('User'):
        """Basic - User object"""
        if not user_email or not isinstance(user_email, str):
            return None
        if not user_pwd or not isinstance(user_pwd, str):
            return None
        try:
            user = User.search({'email': user_email})
        except Exception:
            return None
        if user:
            for i in user:
                if i.is_valid_password(user_pwd):
                    return i
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Complete Basic authentication"""

        auth_header = self.authorization_header(request=request)
        if not auth_header:
            return None

        extract_64 = self.extract_base64_authorization_header(auth_header)
        if not extract_64:
            return None

        decode_base64 = self.decode_base64_authorization_header(extract_64)
        if not decode_base64:
            return None

        em, passwd = self.extract_user_credentials(decode_base64)
        if not em or not passwd:
            return None

        user_object = self.user_object_from_credentials(em, passwd)

        return user_object
