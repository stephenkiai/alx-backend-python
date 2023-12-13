#!/usr/bin/env python3
"""
Asynchronous generator coroutine that yields
random numbers after a 1-second delay.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator coroutine,loops 10 times, waiting
    1 second each time,yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
