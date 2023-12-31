from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм быстрой сортировки.

    1. Выбираем опорный элемент. Например, первый элемент.
    2. В левую часть отправляем всё что меньше опорного элемента, в правую всё что больше.
    3. К левой и правой части рекурсивно применяет алгоритм быстрой сортировки.

    :param container: последовательность, которую надо отсортировать
    :return: Отсортированная в порядке возрастания последовательность
    """

    if len(container) < 2:
        return container
    start = container[0]
    midl = [i for i in container if i == start]
    left = [i for i in container if i < start]
    right = [i for i in container if i > start]

    return sort(left) + midl + sort(right)

    ...  # реализовать алгоритм быстрой сортировки
