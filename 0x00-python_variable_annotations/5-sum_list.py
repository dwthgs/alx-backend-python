#!/usr/bin/env python3
""" Complex types - list of floats """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Parameters
    ----------
    input_list: List of float numbers

    Return: sum of all elements in input_list as a float
    """
    return sum(input_list)
