#!/usr/bin/env python3
"""
Asynchronous coroutine that takes in 2 int arguments.
"""

from typing import List
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times with
    the specified max_delay and returns the list of delays in
    ascending order.
    """

    delays = [wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*delays))
