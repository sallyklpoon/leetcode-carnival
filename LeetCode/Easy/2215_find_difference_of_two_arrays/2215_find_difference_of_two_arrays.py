"""
2215. Find the Difference of Two Arrays

"""


def find_difference_bf(nums1: list, nums2: list) -> list:
    """
    Return the distinct int in each list that is not present in the other.

    This is a Brute Force solution making use of Python set() and set() methods

    Time Complexity: O(N^2) - for-loop through intersection and search in list
    Space Complexity: O(M) - where M is the number of unique intersect values

    :param nums1: a list of int
    :param nums2: a list of int
    :return: a list containing two lists with int elements

    >>> find_difference_bf([1, 2, 3], [2, 4, 6])
    [[1, 3], [4, 6]]
    """
    # find the unique numbers by comparing set intersection
    # set conversion is O(N)
    # intersection is O(min(m, n)), iteration through the smallest set if its values are in larger set
    set_1, set_2 = set(nums1), set(nums2)
    difference = set_1.difference(set_2).union(set_2.difference(set_1))

    output = [[], []]
    for num in difference:
        if num in nums1:
            output[0].append(num)
        else:
            output[1].append(num)
    return output


def find_difference_v1(nums1: list, nums2: list) -> list:
    """
    Return the distinct int in each list that is not present in the other.

    This method focuses on optimizing time complexity to O(N) by use of hashmap

    Time Complexity: O(N) - seperate loops into dict. Dict search is O(1) with hashing
    Space Complexity: O(M) - where M is the number of unique intersect values

    :param nums1: a list of int
    :param nums2: a list of int
    :return: a list containing two lists with int elements

    >>> find_difference_v1([1, 2, 3], [2, 4, 6])
    [[1, 3], [4, 6]]
    >>> find_difference_v1([1, 2, 3, 3], [1, 1, 2, 2])
    [[3], []]
    """
    diff = dict()
    output = [[], []]
    for num in nums1:
        if num not in diff:
            diff[num] = 0

    for num in nums2:
        if num not in diff:
            diff[num] = 1
        elif not diff[num] or diff[num] == -1:
            diff[num] = -1

    for num, list_num in diff.items():
        if list_num >= 0:
            output[list_num].append(num)

    return output

