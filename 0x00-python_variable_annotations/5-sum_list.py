#!/usr/bin/env python3
"""Complex types - mixed list
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """function which takes a list input_list of floats
    as argument and returns their sum as a float."""
    add: float = 0
    for i in input_list:
        add += i
    return (add)
