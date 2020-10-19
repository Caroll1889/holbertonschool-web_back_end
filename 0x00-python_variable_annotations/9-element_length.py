#!/usr/bin/env python3
"""
Let's duck type an iterable object
"""

from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate the below function’s parameters and return
    values with the appropriate type"""
    return [(i, len(i)) for i in lst]