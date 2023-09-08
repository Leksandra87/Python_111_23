from typing import Sequence


def binary_search(value: int, seq: Sequence) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    if not isinstance(value, int):
        raise TypeError
    if not seq:
        raise ValueError
    if seq[0] != value:
        l_ind = 0
    else:
        return 0
    r_ind = len(seq) - 1
    while l_ind < r_ind:
        middle = l_ind + (r_ind - l_ind) // 2
        if value <= seq[middle]:
            r_ind = middle
        else:
            l_ind = middle + 1
    if seq[l_ind] == value:
        return l_ind
    else:
        raise ValueError(f"Элемента {value} нет")




      # реализовать итеративный алгоритм бинарного поиска
