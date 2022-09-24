"""
1374. Generate a String With Characters That Have Odd Count
"""


def generate_the_string(n: int) -> str:
    """
    Generate a string with odd number of chars as substrings.

    :param n: an int, the length of the return string
    :return: a string

    >>> generate_the_string(1)
    'a'
    >>> generate_the_string(2)
    'ab'
    >>> generate_the_string(5)
    'aaaaa'
    >>> generate_the_string(6)
    'abbbbb'
    """
    output = 'a' * n if n % 2 == 1 else 'a' + 'b' * (n - 1)
    return output

