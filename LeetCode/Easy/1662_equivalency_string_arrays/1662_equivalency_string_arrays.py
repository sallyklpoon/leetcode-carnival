"""
1662. Check If Two String Arrays Are Equivalent

i = 2, x = 0

word1 = ["ab", "c"],
----------------^

j = 1, y = 2
word2 = ["a", "bc"]
----------------^

"""


def array_strings_are_equal_bf(word1: list, word2: list) -> bool:
    return ''.join(word1) == ''.join(word2)


def array_strings_are_equal_v1(word1: list, word2: list) -> bool:
    """
    Return if two list of strings are equivalent.

    Time: O(N) - use of ponters for iteration, one-pass per list
    Space: O(max(M, N)) - where m or n is the longest string between the two lists

    :param word1: a list of strings
    :param word2: a list of strings
    :return: boolean, True if both lists contain the same string, else False

    >>> array_strings_are_equal_v1(["ab", "c"], ["a", "bc"])
    True
    """
    i, j = 0, 0  # track elem in list
    x, y = 0, 0  # track char in word within list
    m, n = "", ""  # track count length of word

    while i < len(word1):
        if x >= len(word1[i]):
            x, i = 0, i + 1
        else:
            m += word1[i][x]
            x += 1

    while j < len(word2):
        if y >= len(word2[j]):
            y, j = 0, j + 1
        else:
            n += word2[j][y]
            y += 1

    return n == m


def array_strings_are_equal_v2(word1: list, word2: list) -> bool:
    """Time exceeded attempt with 1 pass."""
    i, j = 0, 0  # track elem in list
    x, y = 0, 0  # track char in word within list
    m, n = 0, 0  # track count length of word

    while i < len(word1) and j < len(word2):
        if x >= len(word1[i]):
            x, i = 0, i + 1
            continue
        if y >= len(word2[j]):
            y, j = 0, j + 1
            continue

        if word1[i][x] != word2[j][y]:
            return False
        else:
            x, y = x + 1, y + 1
            m, n = m + 1, n + 1

    while i < len(word1):
        if x >= len(word1[i]):
            x, i = 0, i + 1
            continue
        x, m = x + 1, m + 1

    while j < len(word2):
        if y >= len(word2[j]):
            y, j = 0, j + 1
            continue
        y, n = x + 1, n + 1

    return n == m
