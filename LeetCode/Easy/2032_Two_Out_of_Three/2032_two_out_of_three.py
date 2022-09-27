"""
2032. Two Out of Three
"""


def two_out_of_three_bf(nums1: list, nums2: list, nums3: list) -> list:
    """
    Return a list of numbers that exist in at least two of the three given lists.

    'Brute Force' strategy using Python built-in sets.
    Time Complexity: At least O(N) - conversions between data sets requires iteration through each list
    Space Complexity: O(M) - where M is the largest list of unique numbers in a set

    :param nums1: a list of int
    :param nums2: a list of int
    :param nums3: a list of int
    :return: a list of int
    """
    set1, set2, set3 = set(nums1), set(nums2), set(nums3)
    temp1 = set1.intersection(set2)
    temp2 = set2.intersection(set3)
    temp3 = set3.intersection(set1)
    return list(temp1 | temp2 | temp3)


def two_out_of_three_v1(nums1: list, nums2: list, nums3: list) -> list:
    """
    Return a list of numbers that exist in at least two of three given lists.

    Manual process.
    Time Complexity: O(N)
    Space Complexity: O(N) using an extra hashmap

    :param nums1: a list of int
    :param nums2: a list of int
    :param nums3: a list of int
    :return: a list of int
    """
    map1 = dict()
    output = []

    for num in nums1:
        map1[num] = 1

    for num in nums2:
        if num in map1:
            map1[num] = -1 if abs(map1[num]) == 1 else 2
        else:
            map1[num] = 2

    for num in nums3:
        if num in map1:
            map1[num] = -1

    for key, value in map1.items():
        if value == -1:
            output.append(key)

    return output
