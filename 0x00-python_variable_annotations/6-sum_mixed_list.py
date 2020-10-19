#!/usr/bin/env python3
"""
Complex types - mixed list
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """function sum_mixed_list which takes a list of floats and integers and
    returns their sum as a float."""
    total: float = 0
    for i in mxd_lst:
        total += i
    return (total)
