"""
834. Sum of Distances in Tree

"""
from collections import deque


def sum_distances_in_tree_non_op(n: int, edges: list) -> list:
    adj = {i: [] for i in range(n)}
    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])

    sums = {i: [0] * n for i in range(n)}
    q = deque()
    summed = [False] * n
    for v in adj:
        if not summed[v]:
            visited = [False] * n
            q.append(v)
            while q:
                curr_v = q.pop()
                visited[curr_v] = True
                for neighbour in adj[curr_v]:
                    if not visited[neighbour]:
                        sums[v][neighbour] = sums[v][curr_v] + 1
                        q.append(neighbour)
        summed[v] = True

    ans = [0] * n
    for node, levels in sums.items():
        ans[node] = sum(levels)

    return ans
