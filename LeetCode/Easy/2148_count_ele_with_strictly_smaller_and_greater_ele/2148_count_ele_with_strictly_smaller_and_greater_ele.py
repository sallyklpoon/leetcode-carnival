"""
2148. Count elements with strictly smaller and greater elements
"""


def countElements(nums: list) -> int:
    """
    Return the count of elements with strictly smaller and greater elements within nums.

    Time: O(N)
    Space: O(1)

    :param nums: a list of integers
    :return: an integer
    """
    low, high = min(nums), max(nums)
    count = 0

    for num in nums:
        if num != low and num != high:
            count += 1

    return count