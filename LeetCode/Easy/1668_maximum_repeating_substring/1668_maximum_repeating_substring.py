"""
1668. Maximum Repeating Substring
"""


def max_repeating_bf(sequence: str, word: str) -> int:
    """
    Time complexity: O(N^2) - while loop with search through sequence each time.
    Space Complexity: O(N * M) - where M is the multiplier of how long the word_combo can be

    :param sequence:
    :param word:
    :return:
    """
    word_combo = word
    count = 0
    while word_combo in sequence:
        count += 1
        word_combo += word
    return count


def max_repeating(sequence: str, word: str) -> int:
    """
    Return the maximum repeating of the sequence substring in word.

    Time complexity: O(N * M) depending on how many searches are required
    Space complexity: O(1)

    :param sequence: a string
    :param word: a string
    :return: an int

    >>> max_repeating("aaabaaaabaaabaaaabaaaabaaaabaaaabaaaaba", "aaaba")
    5
    """
    max_k, count = 0, 0

    pointer = 0

    while pointer < len(sequence):
        if sequence[pointer:pointer + len(word)] == word:
            count += 1
            pointer += len(word)
            max_k = max(max_k, count)
        else:
            count = 0
            pointer += 1

    return max_k
