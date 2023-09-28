from typing import Union

import networkx as nx


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    min_ = nx.dijkstra_path_length(graph, 0, graph.number_of_nodes() - 1)
    return min_

    ...  # c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = nx.DiGraph()
    li = []  # записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней
    for i in range(len(stairway) - 1):
        li.append((i, i + 1, stairway[i]))
        li.append((i, i + 2, stairway[i + 1]))
    li.append((len(stairway) - 1, len(stairway), stairway[-1]))
    stairway_graph.add_weighted_edges_from(li)
    print(stairway_path(stairway_graph))  # 72
