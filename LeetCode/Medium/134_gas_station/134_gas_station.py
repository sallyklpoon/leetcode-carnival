"""
134. Gas Station

Guaranteed unique solution means if there is a solution, there's only one
path that will be able to go across the circuit.

- Start by finding the station that will allow us to travel to the next
- Continue the cycle until we can reach our original index. If we are unable to
reach it before gas runs out, we return -1
- find the starting index
- loop through with pointer
- start flag to indicate if we have found the start

- find start first by going through the list and finding first viable start

[1, 2, 3, 4, 5]
[3, 4, 5, 1, 2]
-^
i = 0
tank = 0
circuit = False
start = -1
[-2, -2, -2, 3, 3]

"""


def can_complete_circuit_one_pass(gas: list, cost: list) -> int:
    """
    Inspired explanation from: https://www.youtube.com/watch?v=lJwbPZGo05A

    Time O(N)
    Space O(1)
    :param gas: a list of int
    :param cost: a list of int
    :return: an int
    """
    # if we don't have total enough gas to negate costs, there is no answer
    if sum(gas) < sum(cost):
        return -1

    # if we do, there has to be an answer. We find the index where
    # adding to tank is not less than 0, if it is, we will move to next index.
    tank, start = 0, 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            tank = 0
            start = i + 1
    return start


def can_complete_circuit_2n_loop(gas: list, cost: list) -> int:
    """
    A solution inspired by my friend, Owoscar's logic of twice loop, greedy algo.

    Time O(2N) == O(N)
    Space = O(1)

    :param gas: a list of int
    :param cost: a list of int
    :return: an int
    """
    n = len(gas)
    tank, start = 0, 0
    for i in range(n * 2):
        actual_i = i % n
        tank += gas[actual_i] - cost[actual_i]
        if tank < 0:
            tank, start = 0, i + 1
        if i - start >= n:
            return start
    return -1


def can_complete_circuit_bf(gas: list, cost: list) -> int:
    """
    Original brute force solution.

    Time O(N*M)
    Space O(N)

    :param gas: a list of int
    :param cost: a list of int
    :return: an int
    """
    starts = [i for i in range(len(gas)) if gas[i] >= cost[i]]

    circuit, ans = False, -1
    while starts and not circuit:
        start = starts.pop()
        tank = gas[start] - cost[start]
        i = start + 1
        while not circuit:
            if i >= len(gas):
                i = 0
            if i == start:
                circuit = True
                ans = start
                break
            tank += gas[i] - cost[i]
            if tank < 0:
                break
            i += 1
    return ans
