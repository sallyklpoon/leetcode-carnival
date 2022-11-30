"""
1207. Unique Number of Occurrences
"""


def unique_occurrences(arr: list) -> bool:
    """
    Return true if the number of occurrences of each value in the array is unique:

    Time: O(n)
    Space: O(n), store extra set up to n values

    :param arr: list of integers
    :return: a boolean
    """
    counts = {}
    for num in arr:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    return len(set(counts.values())) == len(counts)
