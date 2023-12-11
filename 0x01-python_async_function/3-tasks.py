#!/usr/bin/env python3
"""
Regular function that returns an asyncio.Task.
"""

import asyncio
from typing import Coroutine
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Regular function that returns an asyncio.Task for wait_random.
    """

    loop = asyncio.get_event_loop()
    task: asyncio.Task[Coroutine] = loop.create_task(wait_random(max_delay))
    return task
