#!/usr/bin/env python3
'''6-sum_mixed_list.py'''

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''
    Compute the sum of a list of integers and floats.

    Args:
        mxd_list (List[Union[int, float]]): List containing integers nd floats.

    Returns:
        float: Sum of the elements in the input list
    '''
    return sum(mxd_list)
