from typing import List
from queue import PriorityQueue


def stoneGameVI(aliceValues: List[int], bobValues: List[int]) -> int:
    n = len(aliceValues)
    count, a, b = 0, 0, 0

    q = PriorityQueue()

    for i in range(n):
        a_val, b_val = aliceValues[i], bobValues[i]
        q.put((-(a_val + b_val), -a_val, -b_val))

    while not q.empty():
        rock, count = q.get(), count + 1
        if count % 2 == 1:
            a += abs(rock[1])
        else:
            b += abs(rock[2])

    return 0 if a == b else 1 if a > b else -1


print(stoneGameVI([1, 2], [3, 1]))
