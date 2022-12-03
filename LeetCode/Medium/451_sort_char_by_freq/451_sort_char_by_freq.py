"""
451. Sort Characters By Frequency
"""
from collections import Counter


def frequency_sort(s: str) -> str:
    """
    Return the string sorted by character frequency.

    Time: O(N) - the sort is sorting max 62 different types of char 62 log 62 cancels out to 1
    Space: O(1) - up to the number of different characters that may be possible in the string,
                  which is constant max 62

    :param s: a string
    :return: a string
    """
    freq = {}
    # count frequencies
    for char in s:
        freq[char] = 1 if char not in freq else freq[char] + 1

    # create tuple for sorting
    freq_pairs = [(k, v) for k, v in freq.items()]
    freq_pairs.sort(key=lambda x: x[1], reverse=True)
    return ''.join([x[0] * x[1] for x in freq_pairs])


def frequency_sort_with_counter(s: str) -> str:
    """
    Mostly keep this here because I learned about Counter. Just for fun.
    """
    freq = Counter(s)
    # create tuple for sorting
    freq_pairs = [(k, v) for k, v in freq.items()]
    freq_pairs.sort(key=lambda x: x[1], reverse=True)
    return ''.join([x[0] * x[1] for x in freq_pairs])
