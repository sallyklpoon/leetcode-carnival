"""
2279. Maximum Bags With Full Capacity of Rocks
https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

Notes:
- bags have a max capacity x containing y number of rocks
- remaining capacity for each bag is x - y for every bag
- given the additional number of rocks, we want to fill as many bags as possible
  up to it's maximum capacity
- return the number of bags that are completely full when we have dispersed the rocks to maximize
  the number of full bags

Strategy:
- To ensure we have as many full bags as possible, we should always fill bags
  that are closest to its max capacity, meaning those with lowest x - y values should be filled first
- Find remaining capacity, store the bag number and remaining capacity as tuple (list of tuples)
- Sort the list of tuples by remaining capacity
- Iterate through the list of tuple and fill the bags with the additional rocks
- Sum the remaining capacities that == 0

capacity: [91,54,63,99,24,45,78]
rocks   : [35,32,45,98, 6, 1,25]
additional_rocks: 17

bags = [[0, 56], [1, 22], [2, 18], [3, 1], [4, 18], [5, 44], [6, 53]]
[[3, 1], [2, 18], [4, 18], [1, 22], [5, 44], [6, 53], [0, 56]]

[[3, 1], [2, 18], [4, 18], [1, 22], [5, 44], [6, 53], [0, 56]]
--------------^
rocks = 0
"""


def maximum_bags(capacity: list, rocks: list, additional_rocks: int) -> int:
    """
    Return the maximum number of bags with max capacity filled given additional rocks.

    Time: O(N log N), sorting
    Space: O(N)

    :param capacity: a list of int
    :param rocks: a list of int
    :param additional_rocks: an int
    :return: an int
    """
    bags = [[i, capacity[i] - rocks[i]] for i in range(len(capacity))]
    bags.sort(key=lambda x: x[1])
    rocks = 0
    for bag in bags:
        capacity = bag[1]
        if rocks + capacity >= additional_rocks:
            bag[1] -= additional_rocks - rocks
            break
        rocks += bag[1]
        bag[1] = 0
    return sum([1 for bag in bags if bag[1] == 0])
