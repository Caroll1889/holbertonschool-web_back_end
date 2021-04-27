#!/usr/bin/env python3
"""Redis basic
"""

import redis
import sys
from functools import wraps
from uuid import uuid4
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """
    Function that counts how many times methods of
    the Cache class are called.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        Function that increments the count for that key
        every time the method is called
        """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


@count_calls
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
            fn: Optional[Callable] = None) -> Union[str, int, float, bytes]:
        """
        Reading from Redis
        """
        if fn:
            return fn(self._redis.get(key))
        else:
            return self._redis.get(key)

    def get_str(self, data: bytes) -> str:
        """Function that converts bytes in string"""
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """Function that converts bytes in integer"""
        byte_order = sys.byteorder
        return int.from_bytes(data, byte_order)
