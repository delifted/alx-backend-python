#!/usr/bin/env python3
'''7-to_kv.py'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Convert a string key and an int or float value to a tuple.
    The second element of the tuple is the square of the int/float value.'''
    return k, v * v  # Square the value and return a tuple
