"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    _min = arr[0]
    _min_index = 0
    for i in range(1, len(arr)):
        if arr[i] < _min:
            _min = arr[i]
            _min_index = i
    return _min_index
