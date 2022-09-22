"""
724. Find pivot index

[1, 7, 3,]

[1, 8, 11]
----^
right - current index val = right side sum
left = left side sum


[1,7,3,6,5,6]

[1, 8, 11, 17, 22, 28]
---------------^

1: 1 vs 11-8 = 3 -- x
2: 8 vs 17 - 11 = 6 -- x
3: 11 vs 22 - 17 = 5 -- x

"""


def pivot_index_bf(nums: list) -> int:
    """

    :param nums:
    :return:

    >>> pivot_index_bf([1, 7, 3, 6, 5, 6])
    3
    >>> pivot_index_bf([1, 2, 3])
    -1
    >>> pivot_index_bf([2, 1, -1])
    0
    """
    added_bw = [num for num in nums]

    # go forward and sum everything
    for i in range(1, len(added_bw)):
        added_bw[i] += added_bw[i - 1]

    # go backward and sum everything + compare
    for i in range(2, len(nums) - 1):
        if nums[-i] + nums[-i + 1] == added[-i - 2]:
            return len(nums) - i - 1
        else:
            nums[-i] += nums[-i + 1]

    return 0 if nums[1] + nums[2] == 0 else -1
