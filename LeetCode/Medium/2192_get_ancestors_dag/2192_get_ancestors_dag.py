"""
For every ans[i], it will be list of ancestors for i node.

- Topological sort because it asks for order of ancestors
   - consider tasks where you need to queue some tasks before others
- get the in-degrees of each node and start with those that have 0 (means we've explored any ancestors they may have)
- for every child of a node, they must add the node as an ancestor and the node's explored ancestors
"""
from collections import deque
from sortedcontainers import SortedSet


class Solution:
    def getAncestors(self, n: int, edges: list) -> list:
        stack = deque()
        nodes = {i: {'indegrees': 0, 'children': set()} for i in range(n)}
        ans = [SortedSet() for _ in range(n)]

        for src, dest in edges:
            nodes[src]['children'].add(dest)
            nodes[dest]['indegrees'] += 1

        for node in nodes.keys():
            if nodes[node]['indegrees'] == 0:
                stack.append(node)

        while stack:
            curr_node = stack.popleft()
            for child in nodes[curr_node]['children']:
                nodes[child]['indegrees'] -= 1
                # add the current node as an ancestor
                ans[child].add(curr_node)
                # any ancestors of curr node is neighbor's ancestor
                ans[child].update(ans[curr_node])
                if nodes[child]['indegrees'] == 0:
                    stack.append(child)

        return ans
