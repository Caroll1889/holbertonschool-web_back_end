#!/usr/bin/env python3
"""
Complex types - list of floats
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """function sum_list which takes a list of floats as argument and
    returns their sum as a float."""
    suma: float = 0
    for i in input_list:
        suma += i
    return (suma)
