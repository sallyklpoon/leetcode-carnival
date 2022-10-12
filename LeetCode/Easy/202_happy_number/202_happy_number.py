"""
202. Happy Number
"""


def is_happy(n: int) -> bool:
    """

    :param n:
    :return:

    >>> is_happy(1111111)
    true
    """
    squares = [int(x) ** 2 for x in str(n)]
    sum_squares = sum(squares)
    if sum_squares == 1:
        return True
    if sum_squares < 10:
        return False
    return is_happy(sum_squares)
