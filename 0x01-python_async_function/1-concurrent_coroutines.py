#!/usr/bin/env python3
"""execute multiple coroutines"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function that return the list of all the delays (float values)"""
    delays = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
