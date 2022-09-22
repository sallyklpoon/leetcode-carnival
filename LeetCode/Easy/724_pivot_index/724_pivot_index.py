"""
724. Find pivot index

[1, 7, 3,]

[1, 8, 11]
----^
right - current index val = right side sum
left = left side sum


[1,7,3,6,5,6]

[28, 27, 20, 17, 11, 6]
[1, 8, 11, 17, 22, 28]
--------^-------^

1: 1 vs 11-8 = 3 -- x
2: 8 vs 17 - 11 = 6 -- x
3: 11 vs 22 - 17 = 5 -- x

[2, -1, 1]

[2, 1, 2]
[2  0 , 1]

"""


def pivot_index_bf(nums: list) -> int:
    """
    Return the pivot index of a list of int.

    Time Complexity: O(N) - pass 3 times
    Space Complexity: O(N) - stores an extra list

    :param nums: a list of int
    :return: an int, the pivot index

    >>> pivot_index_bf([1, 7, 3, 6, 5, 6])
    3
    >>> pivot_index_bf([1, 2, 3])
    -1
    >>> pivot_index_bf([2, 1, -1])
    0
    >>> pivot_index_bf([-1,-1,0,1,0,-1])
    4
    """
    added_bw = [num for num in nums]

    # go backwards, sum everything
    for i in range(-2, -(len(added_bw) + 1), -1):
        added_bw[i] += added_bw[i + 1]

    # go forward sum everything + compare
    for j in range(1, len(nums)):
        nums[j] += nums[j - 1]

    for k in range(len(nums)):
        if added_bw[k] == nums[k]:
            return k

    return -1
