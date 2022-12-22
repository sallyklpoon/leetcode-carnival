"""
876. Possible Bi-partition
Graph problem, directional.

Traversing the graph, we must check
if a given v dislikes another vertice's neighbours.

For every node, we skip the nodes closest to it. Those must be group 2.

Use two-colour graph
"""
from collections import deque


def possible_bipartition(n: int, dislikes: list) -> bool:
    """
    Return if it's possible to split a set of people into two groups.

    BFS bidirectional graph, for any given vertex, colour it as opposite to its assigned neighbours

    :param n: the number of people, or vertices
    :param dislikes: the edges of a graph, dislikes
    :return: a boolean
    """
    adj_list = {i: [] for i in range(1, n + 1)}
    for dislike in dislikes:
        adj_list[dislike[0]].append(dislike[1])
        adj_list[dislike[1]].append(dislike[0])

    q = deque()
    visited = [False] * (n + 1)
    color = [0] * (n + 1)
    assigned = [False] * (n + 1)
    bipartite = True
    for node in range(1, n + 1):
        if not visited[node]:
            q.append(node)
            while q and bipartite:
                v = q.popleft()
                visited[v] = True
                for neighbour in adj_list[v]:
                    if visited[neighbour]:
                        if not assigned[v]:
                            color[v] = not color[neighbour]
                            assigned[v] = True
                        if assigned[v] and color[v] == color[neighbour]:
                            bipartite = False
                    if not visited[neighbour]:
                        q.append(neighbour)
                assigned[v] = True
    return bipartite
