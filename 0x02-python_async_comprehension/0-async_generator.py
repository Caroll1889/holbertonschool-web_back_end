#!/usr/bin/env python3
"""
Async Generator
"""

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """Async Generator """
    for _ in range(10):
        yield random.random()
        await asyncio.sleep(1)
