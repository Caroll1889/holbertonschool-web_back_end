#!/usr/bin/env python3
"""Hash password
"""

import bcrypt
from db import DB
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> str:
    """Function that return a salted password"""
    salt = bcrypt.gensalt()
    password = bytes(password.encode('utf-8'))
    return bcrypt.hashpw(password, salt)


def _generate_uuid() -> str:
    """Function that return a string representation of a new UUID"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Constructor
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f'User {email} already exists')
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                password = bytes(password.encode('utf-8'))
                return bcrypt.checkpw(password, user.hashed_password)
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """Get session ID"""

        try:
            user = self._db.find_user_by(email=email)
            new_uuid = str(uuid.uuid4())
            self._db.update_user(user.id, session_id=new_uuid)
            return new_uuid
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Find a user by session ID"""
        if not session_id:
            return None

        try:
            user = user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Function that destroys a session"""
        self._db.update_user(user_id, session_id=None)
