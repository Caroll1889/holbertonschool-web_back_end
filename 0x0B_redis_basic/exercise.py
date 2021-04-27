#!/usr/bin/env python3
"""Redis basic
"""

import redis
from uuid import uuid4
from typing import Union, Callable, Optional
import sys


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

    def get(self, key: str,
            fn: Optional[Callable]) -> Union[str, int, float, bytes]:
        """
        Reading from Redis
        """
        try:
            result = self._redis.get(key)
            if fn:
                return fn(result)
            else:
                return result
        except Exception:
            pass

    def get_str(self, data: bytes) -> str:
        """Function that converts bytes in string"""
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """Function that converts bytes in integer"""
        byte_order = sys.byteorder
        return int.from_bytes(data, byte_order)
