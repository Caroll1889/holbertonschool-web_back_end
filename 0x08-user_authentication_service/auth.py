#!/usr/bin/env python3
"""Hash password
"""

import bcrypt


def _hash_password(password: str) -> str:
    """Function that return a salted password"""
    salt = bcrypt.gensalt()
    password = bytes(password.encode('utf-8'))
    return bcrypt.hashpw(password, salt)
