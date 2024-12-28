#!/usr/bin/env python3

"""
A module for adding two numbers.

Module contents:
    - add_numbers: Adds two numbers and returns their sum.

Created on 2024-12-06
Author: GitHub Copilot
"""


def add_numbers(num1, num2):
    """Returns the sum of two numbers.

    Takes two numbers (integers or floats) and returns their sum.
    The output type will match the input types (i.e., if both inputs are integers, the
    output will be an integer; if both are floats, the output will be a float).

    Parameters:
        num1: int or float, the first number to add
        num2: int or float, the second number to add

    Returns -> int or float: the sum of num1 and num2

    Raises:
        AssertionError: if inputs are not both int or float

    Examples:
        >>> add_numbers(5, 3)
        8
        >>> add_numbers(4.5, 3.5)
        8.0
        >>> add_numbers(-2, 6)
        4
    """
    assert isinstance(num1, (int, float)), "num1 must be an int or float"
    assert isinstance(num2, (int, float)), "num2 must be an int or float"

    return num1 + num2
