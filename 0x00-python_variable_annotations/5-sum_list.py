#!/usr/bin/env python3
"""
A type-annotated function sum_list.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floats.
    """
    return sum(input_list)
