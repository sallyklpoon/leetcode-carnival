"""
1971. Find if Path Exists in Graph
https://leetcode.com/problems/find-if-path-exists-in-graph/description/

To find a path between a source and destination, we can choose bfs or dfs.
Practice BFS, I'll use BFS!
"""
from collections import deque


def valid_path(n: int, edges: list, source: int, destination: int) -> bool:
    """
    Check if a valid path exists between a source and destination in a graph.

    Time: up to O(N^2)
    Space: O(N*M) for N number of vertices with M neighbouring nodes

    :param n: an int, the number of vertices
    :param edges: a list of len 2 lists, the edges
    :param source: an int, source vertex number
    :param destination: an int, destination vertex number
    :return: a boolean
    """
    if source == destination:
        return True

    adj = {i: [] for i in range(n)}
    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])

    q = deque([source])
    visited = [False] * n
    while q:
        v = q.popleft()
        visited[v] = True
        for neighbour in adj[v]:
            if neighbour == destination:
                return True
            if not visited[neighbour]:
                q.append(neighbour)
    return False
