"""
1791. Find Center of Star Graph

As defined by the problem, the center of the graph is a node
that connects to every other node.

The restraints of the problem make it much more simple!
We simply need to find the number that exists in all the edges provided.

One approach:
- use a map to track all the count of nodes in the full list. One pass
- return the node that has a sum of n-1 count
"""


def find_center(edges):
    edge_count = {i: 0 for i in range(1, len(edges) + 2)}
    for edge in edges:
        edge_count[edge[0]] += 1
        edge_count[edge[1]] += 1

    for node, count in edge_count.items():
        if count == len(edges):
            return node
