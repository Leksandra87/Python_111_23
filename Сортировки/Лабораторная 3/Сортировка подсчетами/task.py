from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    if len(container) < 2:
        return container
    n = max(container)
    res = [0 for _ in range(n + 1)]
    for val in container:
        res[val] += 1
    _sorted = []
    for key, val in enumerate(res):
        step = [key for _ in range(val)]
        _sorted += step

    return _sorted

    # реализовать алгоритм сортировки подсчетами
