#!/usr/bin/env python3
"""
Complex types - string and int/float to tuple
"""

from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function to_kv that takes a string and an int OR float as
    arguments and returns a tuple
    """
    new: Tuple[str, Union[int, float]] = (k, v**2)
    return (new)
