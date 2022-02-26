from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    _len = len(arr) - 1
    mid = _len // 2
    max_ind = _len
    min_ind = 0
    print(arr)
    print(elem)
    while True:
        print(min_ind, mid, max_ind)
        if arr[mid] > elem:
            max_ind = mid
            min_ind = 0
            mid = (max_ind - min_ind) // 2
        elif arr[mid] < elem:
            min_ind = mid
            mid = (max_ind - min_ind) // 2 + min_ind
        elif arr[mid] == elem:
            return mid


if __name__ == '__main__':
    pass