"""
1557. Minimum Number of Vertices to Reach All Nodes

We want the min list of all the vertices that allows us to reach all vertices in the graph

Based on discussion suggestion:
- We must consider that every node can either be visited or not visited by another node
- We must visit those nodes that can't be visited by other nodes

1. For every edge combo, we check which vertices are visited by another vertex
2. Find those vertices that cannot be visited by another vertex
3. Those that cannot be visited are the answer
"""


def find_smallest_set_of_vertices(n, edges) -> list:
    """
    Time: O(N)
    Space: O(N)

    :param n: the number of vertices
    :param edges: the edges
    :return: a list of min vertices we must visit
    """
    visited = [0] * n
    for edge in edges:
        visited[edge[1]] = 1

    ans = []
    for i in range(n):
        if not visited[i]:
            ans.append(i)

    return ans
