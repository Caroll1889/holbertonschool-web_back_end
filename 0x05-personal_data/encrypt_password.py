#!/usr/bin/env python3
"""Encrypting passwords"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hashed a password"""
    salt = bcrypt.gensalt()
    password = bytes(password.encode('utf-8'))
    return bcrypt.hashpw(password, salt)
