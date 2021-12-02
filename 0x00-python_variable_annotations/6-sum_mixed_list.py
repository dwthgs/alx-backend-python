#!/usr/bin/env python3
""" Complex types - mixed list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Parameters
    ----------
    mxd_lst: mixed List of integers or floats

    Return: sum of all elements in mxd_lst as a float
    """
    return sum(mxd_lst)
