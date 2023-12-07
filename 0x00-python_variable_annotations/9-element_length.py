#!/usr/bin/env python3
"""function parameters annotation"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, each containing an element from the input list
    and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
