"""
1913. Maximum Product Difference Between Two Pairs

We are looking for

max product - min product
"""


def max_product_difference_bf(nums: list) -> int:
    """
    Return max product difference in a list of integers.

    Time Complexity: O(N log N) - transformation by sorting nums
    Space Complexity: O(1)

    :param nums: a list of nums
    :return: an int, the maximum product difference
    """
    nums.sort()
    return nums[-1] * nums[-2] - nums[0] * nums[1]


def max_product_difference(nums: list) -> int:
    """
    Return max product difference in a list of integers.

    Time Complexity: O(N) implementation, but comparable to bf solution above
    Space Complexity: O(1)

    :param nums: a list of nums
    :return: an int, the maximum product difference

    >>> max_product_difference([5, 6, 2, 7, 4])
    34
    """
    smallest, second_smallest = float('inf'), float('inf')
    largest, second_largest = 0, 0

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num >= largest or num > second_largest:
            second_largest = num

    for num in nums:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num <= smallest or num < second_smallest:
            second_smallest = num

    return largest * second_largest - smallest * second_smallest
