"""
797. All Paths From Source to Target

We are looking for all possible paths from 0 to the very last node
- Acyclic, we don't have to check for cycles
- We will need to do DFS to find paths
- Keep track of the last node to have a stack of the path so far leading to end node
- When we reach node (n-1), we append the stack trace to the ans
"""


def all_paths_source_target(graph) -> list:
    """
    Return all the possible paths from 0 to n-1

    Time: Recursive
    Space: O(N) - N nodes

    :param graph: a list of nodes that each graph node i can visit
    :return: a list of possible paths from 0 to n-1
    """

    n, path, ans = len(graph), [], [],

    def dfs(v, n_path):
        n_path.append(v)
        if v == n - 1:
            ans.append(n_path.copy())
        for neighbour in graph[v]:
            dfs(neighbour, n_path)
        n_path.pop()

    dfs(0, path)
    return ans
