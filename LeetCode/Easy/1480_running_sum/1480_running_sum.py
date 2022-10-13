"""
1480. Running Sum
"""


def running_sum(nums: list) -> list:
    """
    Return the running sum of each index in the list.

    Time Complexity: O(N)
    Space Complexity: O(1) - no additional space, returning the input

    :param nums: a list of numbers
    :return: a list of numbers
    """
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums
