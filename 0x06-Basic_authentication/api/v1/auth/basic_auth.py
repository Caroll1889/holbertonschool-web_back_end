#!/usr/bin/env python3
"""Auth class
"""

from api.v1.auth.auth import Auth


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
