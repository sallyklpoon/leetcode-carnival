"""
2206. Divide Array Into Equal Pairs
"""


def divide_array(nums: list) -> bool:
    """
    Determine if the array can be divided into n pairs.

    Time Complexity: O(N) - depending on nums length
    Space Complexity: O(N/2) - half of the list length or smaller

    :param nums: a list of integers
    :return: a boolean
    """
    count_nums = dict()

    for num in nums:
        count_nums[num] = 1 if num not in count_nums else count_nums.get(num) + 1

    for val in count_nums.values():
        if val % 2 != 0:
            return False

    return True
