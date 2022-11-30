"""
33. Search in Rotated Sorted Array.
"""


def search(nums: list, target: int) -> int:
    """
    Find the index of a target integer in a rotated, sorted array in O(log n) time.

    Time: O(log n) , binary search
    Space: O(1), store l and r

    :param nums: a list of int
    :param target: an int
    :return: an int, the index of the target or -1 if not found

    >>> search([3,1], 1)
    1
    """
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l + ((r - l) // 2)
        if nums[mid] == target:
            return mid

        # if left is sorted
        if nums[l] <= nums[mid]:
            in_left = nums[l] <= target < nums[mid]
        else:
            # right is sorted, check right
            in_left = not (nums[mid] < target <= nums[r])

        if in_left:
            r = mid - 1
        else:
            l = mid + 1
    return -1
