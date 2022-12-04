"""
average difference == abs of:

x = avg of first (i+1) elements
y = avg of the remaining elements excluding the (i + 1) elements

- round down to nearest int

[2, 5, 3, 9, 5, 2]

i = 0
x = [2] / i + 1
y = sum[5, 3, 9, 5, 2] / n - i - 1

return index with the min avg difference, if multiple, return smallest
-- return smallest index means we will keep comparing if new avg difference going down list is strictly < stored min


Naive strategy:
- store min, min_i
- iterate through the list and splice to do the math
-- flaw is that we will be doing small iterations each time to sum everything up and basically repeat sums

Second O(N) strategy:
- do cumulative sum from L -> R down the array O(N)
[2, 7, 10, 19, 24, 26]
- iterate second time through array to do the math, but this time, we can take the indexing values, taking O(1) time
to access

i = 0
x = nums[0] / 0 + 1 = 2 / 1
y = nums[-1] - nums[0] / n - i - 1 = 26 - 2 / 6 - 0 - 1

i = 1
x = nums[1]/ 1 + 1 = 7 / 2
y = nums[-1] - nums[0] / 6 - 1 - 1 = 19 / 4

...

Last item is edge case though bc we cannot divide by 0. We can check if we are at the end of the line and simply
return x
i = 5
x = nums[5] / 5 + 1 = 26 / 5
y = nums[-1] - nums[5] / 6 - 5 - 1 = 

"""


def min_avg_difference(nums: list) -> int:
    """
    Return the index with the smallest average difference.

    Time: O(N)
    Space: O(1), re-use input space, only store index and min avg

    :param nums:
    :return:
    """
    min_avg, min_i = float('inf'), 0

    # Create cumulative sum array
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]

    # Do the work of finding min abs difference
    for i in range(len(nums)):
        i_avg = nums[i] // (i + 1)
        if i == len(nums) - 1:
            abs_diff = abs(i_avg)
        else:
            abs_diff = abs(i_avg - ((nums[-1] - nums[i]) // (len(nums) - i - 1)))
        if abs_diff < min_avg:
            min_avg, min_i = abs_diff, i

    return min_i
