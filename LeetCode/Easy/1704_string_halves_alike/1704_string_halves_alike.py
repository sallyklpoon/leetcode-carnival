"""
1704. Determine if String Halves are Alike
"""


def halves_are_alike(s: str) -> bool:
    """
    Return true if string halves contain the same number of vowels.

    Time: O(N)
    Space: O(1)

    :param s: a string of even length
    :return: a bool
    """
    mid = len(s) / 2 - 1
    i = 0
    v_count = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0,
    }
    while i < len(s):
        curr_char = s[i].lower()
        if i <= mid and curr_char in v_count:
            v_count[curr_char] += 1
        if i > mid and curr_char in v_count:
            v_count[curr_char] -= 1
        i += 1
    return sum(v_count.values()) == 0

