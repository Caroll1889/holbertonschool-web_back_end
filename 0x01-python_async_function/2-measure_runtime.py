#!/usr/bin/env python3
"""Measure the runtime
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ function that measures the total execution time"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time() - start_time
    return end_time / n
