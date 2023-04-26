"""
You can only subtract 1 or subtract 2 from n each time
How many combo of sums can we have to add up to n

Base cases:
- 2 step left has 2 ways [1, 1] or [2]
- 1 step left has 1 way [1]

Memoize the n steps to reduce time.
Any n steps is an addition of climbStairs[n - 1] + climbStairs[n - 2] as there are only
two options to do it. This is a fib problem variation!
"""


class Solution:
    def __init__(self):
        self.memo = {}

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        if n in self.memo:
            return self.memo[n]
        ans = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.memo[n] = ans
        return ans
