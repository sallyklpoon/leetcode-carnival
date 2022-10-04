"""
1455. Check if a Word Occurs As a Prefix of Any Word in a Sentence

"""


def is_prefix_of_word(sentence: str, search_word: str) -> int:
    """
    Return the word number of the first occurrence of the prefix in a sentence.

    Time Complexity: O(M) - where N is the number of words in the sentence
    Space Complexity: O(M) - where M is the number of words in the sentence

    :param sentence: a string
    :param search_word: a string, the prefix to be searched
    :return: an int, the word position within the sentence with the prefix (1-indexed)
    """
    words = sentence.split(' ')
    for i, word in enumerate(words):
        if word[:len(search_word)] == search_word:
            return i + 1
    return -1
