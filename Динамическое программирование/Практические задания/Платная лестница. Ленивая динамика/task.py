from typing import Union, Sequence
from functools import lru_cache


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param stairway: список целых чисел, где каждое целое число является стоимостью конкретной ступени
    :return: минимальная стоимость подъема на верхнюю ступень
    """

    @lru_cache()
    def lazy_dim(stairw, n):
        if n == 0 or n == 1:
            return stairw[n]
        return stairw[n] + min(lazy_dim(stairw, n - 1), lazy_dim(stairw, n - 2))

    return lazy_dim(stairway, len(stairway) - 1)

    ...  # реализовать ленивую динамику


if __name__ == '__main__':
    print(stairway_path((1, 3, 1, 5)))  # 7
