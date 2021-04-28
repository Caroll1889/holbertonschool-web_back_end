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


def call_history(method: Callable) -> Callable:
    """
     Function that stores the history of inputs and
     outputs for a particular function.
    """
    key = method.__qualname__
    inputs = key + ':inputs'
    output = key + ':outputs'

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Wrapper function"""
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwds)
        self._redis.rpush(output, str(result))
        return result
    return wrapper


def replay():
    """
    Function that displays the history of calls of a particular function.
    """
    red = redis.Redis()
    key = method.__qualname__
    key.decode('utf-8')
    count = red.get(key)
    inputs = r.lrange(name + 'inputs', 0, -1)
    output = r.lrange(name + 'outputs', 0, -1)

    print(f'{key} was called {count} times')
    for inp, out in zip(inputs, output):
        print(f'{key}(*{inp.decode("utf-8")}) -> {out.decode("utf-8")}')


class Cache():
    """Cache class"""
    def __init__(self):
        """
        Constructor
        Stores an instance of the Redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
