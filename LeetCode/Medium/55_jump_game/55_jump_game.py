"""
55. Jump Game
https://leetcode.com/problems/jump-game/

You are given an integer array nums. You are initially positioned at the array's first index, and each element in
the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Start at index 0.

Graph solution:

Perhaps for every index, we can store the indexes we can reach. Then conduct a search.
A possible approach may be BFS to reach the end.

Bi-directional to go back and forth to find the destination.

Goal setting recursive solution:
Go from the back of the list. Find the first index where we can reach the end goal.
Once we find that, continue down the array backwards to find the next one that can reach the new goal index.

- store goal index
- Start from end of list, go backwards
- Find index who's power is >= goal index - current index
- Once found, store this index as the next goal
- Continue doing this down the list. If our final goal index is 0, return True. If it is not (we can't start at 0), return False

[2, 3, 1, 1, 4]
-^
goal i = 0
goal i - curr i = 1

[3, 2, 1, 0, 4]
-^
goal i = 4
goal i - curr i = 1
"""
from collections import deque


def can_jump_one_pass(nums) -> bool:
    """
    Return if it's possible to jump to the end of the array.

    Time: O(N)
    Space: O(1)

    Approach is one-pass, setting a new goal for new achievement each time we can reach
    the most recent goal. If we can jump to the end, our final goal should be index 0,
    which is where we begin.

    :param nums: an array of int
    :return: a boolean
    """
    goal = len(nums) - 1
    i = len(nums) - 2
    while i >= 0:
        steps_needed = goal - i
        if nums[i] >= steps_needed:
            goal = i
        i -= 1
    return goal == 0


def bfs_can_jump(nums) -> bool:
    """
    Return if it's possible to jump to the end of the array.

    Time: O(N*M) for each node, there's M possible neighbours that will be generated
    Space: O(N)

    Not an optimal solution because it will generate all possibilities to search.

    :param nums: an array of int
    :return: a boolean
    """
    n = len(nums)
    adj = {i: [] for i in range(n)}
    for i in range(n - 1):
        for steps in range(1, nums[i] + 1):
            dest_node = i + steps
            if dest_node < n:
                adj[i].append(dest_node)
                adj[dest_node].append(i)

    visited = [False] * n
    q = deque([0])
    target = n - 1

    while q:
        node = q.popleft()
        if node == target:
            return True
        visited[node] = True
        for neighbour in adj[node]:
            if not visited[neighbour]:
                q.append(neighbour)
    return False
