#!/usr/bin/env python3
"""Add type annotations to function safely_get_value"""
from typing import TypeVar, Dict, Any, Optional


K = TypeVar('K')
V = TypeVar('V')


def safely_get_value(dct: Dict[K, V], key: K, default: Optional[V] = None) -> V:
    """
    Safely gets the value associated with the given key from a dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
