"""
2192. All Ancestors of a Node in a Directed Acyclic Graph

"""


def get_ancestors(n, edges) ->  list:
    visitable = [0] * n
    adj = {i: [] for i in range(n)}
    for edge in edges:
        adj[edge[0]].append(edge[1])
        visitable[edge[1]] = 1

    ans = [[] for _ in range(n)]

    def dfs(v, call_stack):
        call_stack.append(v)
        for neighbour in adj[v]:
            ans[neighbour].extend(call_stack)
            dfs(neighbour, call_stack)
        call_stack.pop()

    for j in range(n):
        if not visitable[j]:
            dfs(j, [])

    for i in range(n):
        ans[i] = sorted(list(dict.fromkeys(ans[i])))

    return ans


print(get_ancestors(8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))
