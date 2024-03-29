#!/usr/bin/env python3
'''
Annotate a function and return values with
the appropriate types.'''

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Return values'''
    return [(i, len(i)) for i in lst]
