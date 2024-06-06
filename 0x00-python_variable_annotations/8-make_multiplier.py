#!/usr/bin/env python3
""" make multiplier """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ return function that multiplies """
    def multiply(x: float) -> float:
        """ multiply """
        return x * multiplier
    return multiply
