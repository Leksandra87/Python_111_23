from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм сортировки слиянием.

    1. Если массив состоит из 1 элемента – он отсортирован
    2. Иначе массив разбивается на две части, которые сортируются рекурсивно
    3. После сортировки двух частей массива к ним применяется процедура слияния

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """

    def _merge(li_1: List[int], li_2: List[int]) -> List[int]:
        merged = []
        while True:
            if not li_1:
                merged += li_2
                return merged
            if not li_2:
                merged += li_1
                return merged
            if li_1[0] <= li_2[0]:
                merged.append(li_1.pop(0))
            else:
                merged.append(li_2.pop(0))

    if len(container) < 2:
        return container
    midl = len(container) // 2
    left = sort(container[:midl])
    right = sort(container[midl:])
    return _merge(left, right)

    #  реализуйте сортировку слиянием
