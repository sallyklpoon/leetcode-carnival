"""
392. Is Subsequence
"""


def is_subsequence(s: str, t: str) -> bool:
    """
    Determine if a sequence, s is a subsequence in t.

    Time Complexity: O(N) - where N is the length of t
    Space Complexity: O(1)

    :param s: a string, the sequence to be found
    :param t: a string, the string to search for the sequence
    :return: boolean
    """
    s_count, t_count = 0, 0

    while s_count < len(s) and t_count < len(t):
        if s[s_count] == t[t_count]:
            s_count, t_count = s_count + 1, t_count + 1
        else:
            t_count += 1
    return s_count == len(s)
