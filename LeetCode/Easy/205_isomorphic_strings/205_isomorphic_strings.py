"""
205. Isomorphic Strings

We need a map of the characters between both strings.

Iterate through both strings at the same time, given same length,
Check if the key exists for the key char string
- if not, we will add to map and map the two char
- if yes, check is 2nd string is equal to the mapped char

** missed: we must also track if we've already used a value from 'other string' as value! **
"""


def is_isomorphic(s: str, t: str) -> bool:
    """
    Return if two strings are isomorphic.

    Time Complexity: O(N) - one pass, length of s/t or less
    Space Complexity: O(1) - dict and list will max be up to ASCII character amount 128

    :param s: a string
    :param t: a string
    :return: boolean
    """
    char_map = {}
    seen_char = [0 for i in range(128 + 1)]

    for i in range(len(s)):
        if s[i] in char_map:
            if t[i] != char_map[s[i]]:
                return False
        else:
            if seen_char[ord(t[i])]:
                return False
            char_map[s[i]] = t[i]
            seen_char[ord(t[i])] = 1

    return True
