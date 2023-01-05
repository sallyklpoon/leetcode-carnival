"""
496. Next Greater Element
"""


def next_greater_element(nums1: list, nums2: list) -> list:
    """
    Return next greater elements of a sublist.

    Time O(N^2)
    Space O(1) - ans requires list of nums1

    :param nums1: a list of unique int
    :param nums2: a list of unique int
    :return: a list of int
    """
    ans = [-1 for _ in range(len(nums1))]
    for i in range(len(nums1)):
        num = nums1[i]
        j = nums2.index(num)
        for next_num in nums2[j + 1:]:
            if next_num > num:
                ans[i] = next_num
                break
    return ans
