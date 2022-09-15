"""
12. Roman to Integer
"""

ROMAN_MAP = {'I': 1, 'X': 10, 'C': 100, 'M': 1000, 'V': 5, 'L': 50, 'D': 500}


def roman_to_int(s: str) -> int:
    """
    Return the integer of a Roman Numeral.

    Time Complexity: O(N)
    Space Complexity: O(N) - dependent on string length

    Idea of this implementation is to use a LIFO Stack where the end of the string is the last letter.

    :param s: a string of roman numerals
    :precondition: the string must only contain roman numerals I, X, C, M, V, L, D
    :precondition: the roman numeral string must be a valid roman numeral
    :return: int, the integer translation of the roman numeral

    >>> roman_to_int('')
    0
    >>> roman_to_int('III')
    3
    >>> roman_to_int('LVIII')
    58
    >>> roman_to_int('MCMXCIV')
    1994
    """
    integer = 0
    char_list = [char for char in s]
    while char_list:
        curr_char = char_list.pop()
        integer += ROMAN_MAP[curr_char]
        if char_list and ROMAN_MAP[char_list[-1]] < ROMAN_MAP[curr_char]:
            integer -= ROMAN_MAP[char_list.pop()]
    return integer
