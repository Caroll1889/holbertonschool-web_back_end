#!/usr/bin/env python3
"""Redis basic
"""

import redis
from uuid import uuid4
from typing import Union


class Cache():
    """Cache class"""
    def __init__(self):
        """
        Constructor
        Stores an instance of the Redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method that generates a random key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
