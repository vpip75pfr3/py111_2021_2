"""
Taylor series
"""
import math
from typing import Union
from itertools import count


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    EPSILON = 0.0001
    exp = 1
    for n in count(1, 1):
        cur_exp = (x ** n) / math.factorial(n)
        exp += cur_exp
        if EPSILON > cur_exp:
            break
    return exp


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    print(x)
    return 0
