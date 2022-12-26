"""
172. Factorial Trailing Zeroes
"""


def trailing_zeroes(n: int) -> int:
    count = 0
    f = factorial(n)
    while f % 10 == 0:
        count += 1
        f //= 10
    return count


def factorial(n: int) -> int:
    if n == 1 or n == 0:
        return n
    return n * factorial(n - 1)
