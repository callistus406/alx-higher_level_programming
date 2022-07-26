#!/usr/bin/python3
"""
This module defines `add_integer`
The function returns the sum of a and b
"""


def add_integer(a, b=98):
    """Take the arguments to add.
    a: One of the numbers, default not defined.
    b: The other number, default 98.
    Return: int(a + b)
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
