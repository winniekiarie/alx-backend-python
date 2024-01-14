#!/usr/bin/env python3
'''More involved type annotations'''
from typing import Sequence, Union, Any, TypeVar, Mapping

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    ''' Function safely_get_value '''
    if key in dct:
        return dct[key]
    else:
        return
