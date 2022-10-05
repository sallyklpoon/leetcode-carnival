"""
997. Find the Town Judge

TODO: try implementing with hash map or graph theory
"""


def find_judge(n: int, trust: list) -> int:
    """
    Return the town judge.

    :param n: an int
    :param trust: a list of lists, length 2
    :return: an int, the judge

    >>> find_judge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]])
    3
    """
    temp = [0 for k in range(n)]
    possible_judge = 0

    # find possible judge
    for pair in trust:
        temp[pair[0] - 1] = 1
    for i in range(n):
        if not temp[i]:
            possible_judge = i

    if not possible_judge or not trust:
        return -1

    # check that everyone trusts the judge
    for pair in trust:
        if pair[1] == possible_judge + 1:
            temp[pair[0] - 1] = -1
    for i in range(n):
        if temp[i] != -1 and i != possible_judge:
            return -1

    return possible_judge + 1
