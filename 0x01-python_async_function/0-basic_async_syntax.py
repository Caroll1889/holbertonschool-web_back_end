#!/usr/bin/env python3
"""The basics of async
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine that takes in an integer argument,
    waits for a random delay and eventually returns it."""
    random_range: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_range)
    return (random_range)
