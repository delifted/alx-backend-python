#!/usr/bin/env python3
'''1-concurrent_coroutines.py
Multiplies coroutines at the same time with async
'''

from typing import List
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Multiple coroutines: returns list of all delay (float values)
    in ascending order without using sort()
    '''
    delays = [wait_random(max_delay) for i in range(n)]
    completed = await asyncio.gather(*delays)
    return sorted(completed)