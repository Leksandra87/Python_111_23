"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    if not arr:
        raise ValueError

    ind = 0
    min_num = arr[ind]
    for i, val in enumerate(arr):
        if val < min_num:
            ind = i
            min_num = val
    return ind

    #  реализовать итеративный линейный поиск
