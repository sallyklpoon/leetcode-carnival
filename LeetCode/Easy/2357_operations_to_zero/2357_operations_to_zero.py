"""
2357. Make Array Zero by Subtracting Equal Amounts
"""


def minimum_operations(nums: list) -> int:
    """
    Brute Force finding minimum operations required for a list to be subtracted
    to zero using the smallest non-zero number each time.

    :param nums: a list of int
    :return: an int, the number of operations required
    """
    operations = 0
    while sum(nums) > 0:
        nums = list(filter(lambda num: num > 0, nums))
        x = min(nums)
        nums = list(map(lambda num: num - x, nums))
        operations += 1
    return operations


def minimum_operations_v1(nums: list) -> int:
    """
    Shorter answer!

    :param nums: list of integers
    :return: an int
    """
    return len(set(filter(lambda num: num > 0, nums)))
