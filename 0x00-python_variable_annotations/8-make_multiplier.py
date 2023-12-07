#!/usr/bin/env python3
"""
A type-annotated function make_multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the specified multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiplies a float by the specified multiplier.
        """
        return value * multiplier

    return multiplier_function
