#!/usr/bin/env python3
"""Session Authentication"""

from api.v1.auth.auth import Auth
from uuid import uuid4
from typing import List, TypeVar
from models.user import User


class SessionAuth(Auth):
    """Create a session"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Function that creates a Session ID for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None
        session = str(uuid4())

        self.user_id_by_session_id[session] = user_id
        return session

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """function that returns a User ID based on a Session ID:"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> TypeVar('User'):
        """Function that returns a User instance based on a cookie value"""
        session = self.session_cookie(request)

        if session is None:
            return None

        user = self.user_id_for_session_id(session)

        return User.get(user)

    def destroy_session(self, request=None):
        """Function  that deletes the user session / logout"""
        if request is None:
            return False
        session = self.session_cookie(request)
        if session is None:
            return False
        user = self.user_id_for_session_id(session)
        if not user:
            return False

        del self.user_id_by_session_id[session]
        return True
