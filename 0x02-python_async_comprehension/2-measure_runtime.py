#!/usr/bin/env python3
'''
Task 3 -Async comprehension
'''


import asyncio
from typing import List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Executes async_comprehension 4 times and measures
    the total time of execution
    '''
    start_time = asyncio.get_running_loop().time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = asyncio.get_running_loop().time()
    return end_time - start_time
