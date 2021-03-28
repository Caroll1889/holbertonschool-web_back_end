#!/usr/bin/env python3
"""Encrypting passwords"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hashed a password"""
    salt = bcrypt.gensalt()
    password = bytes(password.encode('utf-8'))
    return bcrypt.hashpw(password, salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Function that check if a password is valid"""
    salt = bcrypt.gensalt()
    password = bytes(password.encode('utf-8'))
    hashed = bcrypt.hashpw(password, salt)
    return bcrypt.checkpw(password, hashed)
