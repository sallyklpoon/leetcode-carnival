"""

Mock Interview Sept 16, 2022
448. Find all numbers disappeared in an array

"""


def num_not_in_list(nums: list) -> list:
    """
    Return the numbers not in a list that should contain list length as range.

    Time Complexity: O(N) - one pass each time with list
    Space Complexity: O(N) - storage of extra list of flags for the numbers

    :param nums: list of int
    :return: list of int

    >>> num_not_in_list([])
    []
    >>> num_not_in_list([1])
    []
    >>> num_not_in_list([3, 1, 2])
    []
    >>> num_not_in_list([4, 4, 2, 5, 4])
    [1, 3]
    """
    upper = len(nums)
    num_tracker = [None for i in range(upper + 1)]
    output = []

    for i in range(upper):
        num_tracker[nums[i]] = True

    for j in range(1, upper + 1):
        if not num_tracker[j]:
            output.append(j)

    return output

