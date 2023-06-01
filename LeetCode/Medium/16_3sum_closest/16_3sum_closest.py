"""
1. pre-sort the numbers
2. have a fixed first number
3. set the left and right, left as the number right after the fixed and right as the end of the list
4. check the difference and update the answer/diff each time
5. if the current sum is less than target, we increment left, if sum is higher than target, decrement the right
"""

def three_sum_closest(nums: list, target: int) -> int:
    nums.sort()
    ans, diff, n = 0, float('inf'), len(nums)
    for i in range(n):
        l, r = i + 1, n - 1
        while l < r:
            curr_sum = nums[i] + nums[l] + nums[r]
            curr_diff = abs(target - curr_sum)
            if curr_diff == 0:
                return curr_sum
            else:
                if curr_diff <= diff:
                    ans = curr_sum
                    diff = curr_diff
                if curr_sum < target:
                    l += 1
                else:
                    r -= 1
    return ans
