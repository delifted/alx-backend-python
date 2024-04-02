#!/usr/bin/env python3
'''3-tasks.py
Function takes an integer and returns and asyncio Task'''

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Returns an asyncio.Task'''
    return asyncio.create_task(wait_random(max_delay))
