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
    return str(uuid.uuid4)


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
