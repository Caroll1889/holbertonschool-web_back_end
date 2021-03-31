#!/usr/bin/env python3
"""Auth class
"""

from api.v1.auth.auth import Auth
import base64


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
