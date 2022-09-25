"""
2255. Count Prefixes of a Given String

"""


def count_prefixes_bf(words: list, s: str) -> int:
    """
    Return the number of words that are prefixes of a given string and list of prefixes.

    Time Complexity: O(N^2) - looping through each word then string comparison of each word
    Space Complexity: O(1)

    :param words: a list of strings, possible prefixes
    :param s: a string
    :return: an int, the count of prefixes of the string, s, in the list words
    """
    count = 0
    for word in words:
        if len(word) <= len(s) and word == s[:len(word)]:
            count += 1
    return count
