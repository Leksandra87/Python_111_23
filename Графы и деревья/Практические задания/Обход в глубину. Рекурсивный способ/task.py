from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в глубину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    visited = {node: False for node in g.nodes}
    path = []

    def recursion(current):
        visited[current] = True
        path.append(current)
        for neighbour in g[current]:
            if not visited[neighbour]:
                recursion(neighbour)

    recursion(start_node)
    return path

    ...  # реализовать обход в глубину


if __name__ == '__main__':
    g = nx.Graph()
    g.add_nodes_from('ABCDEFG')
    g.add_edges_from([
        ('A', 'C'),
        ('A', 'B'),
        ('C', 'F'),
        ('B', 'E'),
        ('B', 'D'),
        ('E', 'G')
    ])

    print(dfs(g, 'A'))
    ...
