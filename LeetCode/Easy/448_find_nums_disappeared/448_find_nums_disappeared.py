"""
448. Find all numbers disappeared in an array
Mock Interview Sept 16, 2022

[-2, -2, 1, 2]
1  , 2, 3, 4

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


def num_not_in_list_better_space(nums: list) -> list:
    """
    Return the numbers not in a list that should contain list length as range.

    Time Complexity: O(N) - two pass
    Space Complexity: O(1) - no extra space needed except for output

    :param nums: list of int
    :return: list of int

    >>> num_not_in_list_better_space([])
    []
    >>> num_not_in_list_better_space([1])
    []
    >>> num_not_in_list_better_space([3, 1, 2])
    []
    >>> num_not_in_list_better_space([4, 4, 2, 5, 4])
    [1, 3]
    """
    for i in range(len(nums)):
        if nums[abs(nums[i]) - 1] > 0:
            nums[abs(nums[i]) - 1] *= -1

    output = []
    for j in range(len(nums)):
        if nums[j] > 0:
            output.append(j + 1)

    return output
