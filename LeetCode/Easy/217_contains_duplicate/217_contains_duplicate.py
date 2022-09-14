"""
217. Contains Duplicate
"""


def contains_duplicate_simple(nums: list) -> bool:
    """
    Return True if a list of number contains duplicates.

    Borrows from built-in library/Python functions, but first solution
    that comes to mind. Rest are solutions that are a little more 'manual'

    :param nums: a list of numbers
    :return: bool, true if the list contains duplicate numbers
    """
    return len(nums) != len(set(nums))


def contains_duplicate_bf(nums: list) -> bool:
    """
    Return True if a list of number contains duplicates. Brute Force.

    Time Complexity: O(N log N) - pre-sorting transformation + O(N) for one-pass
    Space-complexity: O(1) - i and j assignment

    :param nums: a list of numbers
    :return: bool, true if the list contains duplicate numbers
    """
    nums.sort()
    i, j = 0, 1
    while j < len(nums):
        if nums[i] == nums[j]:
            return True
    return False


def contains_duplicate_v1(nums: list) -> bool:
    """
    Return True if a list of number contains duplicates. HashMap solution.

    Time Complexity: O(N), one-pass
    Space Complexity: O(N), possibility ot storing up to N keys in dict.

    :param nums: a list of numbers
    :return: bool, true if the list contains duplicate numbers
    """

    count_map = dict()

    # Get count of numbers O(N)
    for num in nums:
        count_map[num] = 1 if num not in count_map.keys() else (count_map[num] + 1)

        # End and return True if we have count greater than 1
        if count_map[num] > 1:
            return True
    return False
