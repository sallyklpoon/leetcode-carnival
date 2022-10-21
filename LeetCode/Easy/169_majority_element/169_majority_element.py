"""
169. Majority Element
"""


def majority_element(nums: list) -> int:
    """
    Time: O(N) - single iteration up to the end of the list length
    Space: O(N) - variable depending on nums unique elements

    :param nums: a list of int
    :return: an int
    """
    majority_count = len(nums) // 2
    occurrences = dict()

    for num in nums:
        occurrences[num] = 1 if num not in occurrences else occurrences.get(num) + 1
        if occurrences[num] > majority_count:
            return num
