"""
1657. Determine if Two Strings Are Close
https://leetcode.com/problems/determine-if-two-strings-are-close/description/

RULES:
- w1 and w2 must have equal length
- must contain only the same chars
- must have the same duplications or counts per char

"abc" - "bca"
[*] rule 1
[*] rule 2
[*] rule 3

"a" - "aa"
[x] rule 1 -- broken, so false
[*] rule 2
[x] rule 3 -- also broken, so false

"cabbba" - "abbccc"
[*] rule 1
[*] rule 2
[*] rule 3
"""
from collections import Counter


def close_strings(word1: str, word2: str) -> bool:
    """
    Determine if two strings are close.

    Time: O(N) - sorted is 26 log 26 characters, cancelling each other out
    Space: O(N)

    :param word1: a string
    :param word2: a string
    :return: a boolean
    """
    if len(word1) != len(word2) or set(word1) != set(word2):
        return False

    dup_count_w1, dup_count_w2 = {}, {}

    for char in word1:
        dup_count_w1[char] = 1 if char not in dup_count_w1 else dup_count_w1.get(char) + 1

    for char in word2:
        dup_count_w2[char] = 1 if char not in dup_count_w2 else dup_count_w2.get(char) + 1

    return sorted(list(dup_count_w2.values())) == sorted(list(dup_count_w1.values()))


def close_strings_cheat(word1: str, word2: str) -> bool:
    if len(word1) != len(word2) or set(word1) != set(word2):
        return False
    return sorted(list(Counter(word1).values())) == sorted(list(Counter(word2).values()))
