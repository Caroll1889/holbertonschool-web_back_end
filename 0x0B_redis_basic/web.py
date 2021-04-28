#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""

import requests
from typing import Callable
from functools import wraps
import redis

red = redis.Redis()


def count_times(method: Callable) -> Callable:
    """Function that tracks how many times a particular URL was
    accessed in the key
    """
    @wraps(method)
    def wrapper(url):
        """wrapper function"""
        red.incr(f'count:{url}')
        page = red.get(url)
        if page:
            return page.decode('utf-8')
        html_page = method(url)
        red.setex(url, 10, html_page)
        return html_page
    return wrapper


@count_times
def get_page(url: str) -> str:
    """Function that obtains the HTML content of a particular URL
    and returns it.
    """
    response = requests.get(url)
    return response.text
