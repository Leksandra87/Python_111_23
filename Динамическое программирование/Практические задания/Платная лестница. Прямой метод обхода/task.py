from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param stairway: список целых чисел, где каждое целое число является стоимостью конкретной ступени
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    count_stairs = len(stairway)
    if count_stairs == 1:
        return stairway[0]
    if count_stairs == 2:
        return stairway[1]
    cost = [0] * count_stairs
    cost[0] = stairway[0]
    cost[1] = stairway[1]
    for cur in range(2, len(stairway)):
        cost[cur] = min(cost[cur - 1], cost[cur - 2]) + stairway[cur]
    return cost[-1]
    ...  #  реализовать прямой метод расчета


if __name__ == '__main__':
    print(stairway_path([1, 3, 1, 5]))  # 7
