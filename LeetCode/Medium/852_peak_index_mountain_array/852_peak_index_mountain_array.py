"""
There is only one single peak point
Noticing O(logN) time, we likely want to use binary search.

- start in the middle, check the value
- if left < mid and mid > right: return index
- if left > mid, search left
- if right < mid, search right
- continue until our right index is higher than left index
"""

def peakIndexInMountainArray(arr: list) -> int:
    """
    Time: O(log n)
    Space: O(1)

    :param arr: an array of indexes with a peak within (not at the edges)
    :return: the index of the peak
    """
    n = len(arr)
    l, r = 0, n - 1

    while l <= r:
        mid = l + (r - l) // 2

        # Python list indexes cyclic, so we need these cases to skip the edge
        if mid == 0:
            l += 1
            continue
        if mid == n - 1:
            r -= 1
            continue

        # BS value here
        mid_val, left_val, right_val = arr[mid], arr[mid - 1], arr[mid + 1]
        if mid_val > left_val and mid_val > right_val:
            return mid
        if left_val > mid_val:
            r = mid - 1
        elif left_val < mid_val:
            l = mid + 1

    return -1

peakIndexInMountainArray([3,9,8,6,4])
