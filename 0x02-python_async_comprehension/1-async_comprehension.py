#!/usr/bin/env python3
'''1-async_comprehension.py'''


import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Returns 10 random figures
    '''
    return [x async for x in async_generator()]
