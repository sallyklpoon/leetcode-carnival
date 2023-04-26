class SolutionMemo:
    """
    Practice using memo for dynamic programming
    """

    def __init__(self):
        self.memo = {}

    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        if n in self.memo:
            return self.memo[n]
        return self.fib(n - 1) + self.fib(n - 2)


class SolutionRecursive:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
