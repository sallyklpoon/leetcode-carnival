"""
841. Keys and Rooms

Keep track of whether rooms have been visited with 1 or 0,
we can get the sum of the map values at the end to determine if we visited all.

We can also use a queue to track the keys that we have obtained for
all the rooms. When we visit a room, we can extend this queue with the keys
We continue until queue is exhausted.

Start by visiting room 0.
"""
from collections import deque


def can_visit_all_rooms(rooms):
    """
    Return if all rooms can be visited with given keys in the sub-arrays.

    Time O(N) - queue
    Space O(N) - extra space for storing visited
    :param rooms:
    :return:
    """
    visited = [0 for i in range(len(rooms))]
    visited[0] = 1
    keys = deque(rooms[0])

    while keys:
        i = keys.popleft()
        if not visited[i]:
            visited[i] = 1
            keys.extend(rooms[i])

    return sum(visited) == len(rooms)


print(can_visit_all_rooms([[1, 3], [3, 0, 1], [2], [0]]))
