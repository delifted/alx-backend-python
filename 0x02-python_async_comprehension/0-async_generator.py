#!/usr/bin/env python3
'''0-async_generator.py
Async generator
'''


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    Yields number between 0 and 10
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
