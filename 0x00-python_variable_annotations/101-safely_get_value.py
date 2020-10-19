#!/usr/bin/env python3
"""
More involved type annotations
"""

from typing import Mapping, Any, TypeVar, Union

T_Var = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T_Var, None] = None
                     ) -> Union[Any, T_Var]:
    """add type annotations to the function"""
    if key in dct:
        return dct[key]
    else:
        return default
