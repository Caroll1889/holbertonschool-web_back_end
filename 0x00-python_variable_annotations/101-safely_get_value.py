#!/usr/bin/env python3
"""More involved type annotations
"""

from typing import TypeVar, Union, Any, Mapping

t_var = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[t_var, None] = None) -> Union[Any, t_var]:
    if key in dct:
        return dct[key]
    else:
        return default
