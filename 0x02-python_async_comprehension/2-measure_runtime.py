#!/usr/bin/env python3
"""
Coroutines for measuring the total runtime of async_comprehension
executed four times in parallel.
"""

import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using asyncio.gather
    and measures the total runtime.
    """
    start_time = asyncio.get_event_loop().time()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())

    total_time = asyncio.get_event_loop().time() - start_time
    return total_time
