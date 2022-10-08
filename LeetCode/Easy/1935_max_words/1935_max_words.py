"""
1935. Maximum Number of Words You Can Type
"""


def can_be_typed_words(text: str, brokenLetters: str) -> int:
    """
    Brute force solution.

    Time Complexity: O(N^3)
    Space

    :param text: a string
    :param brokenLetters: a string
    :return: an int, the number of words that can be completed
    """
    count = 0
    words = text.split(' ')
    for word in words:
        for letter in brokenLetters:
            if letter in word:
                count += 1
                break
    return len(words) - count
