"""
290. Word Pattern

For every word, we can assign a pattern string to it and match

- transform sentence into word list
- iterate through pattern
- iterate through word list

- if the pattern char is in a map that we bank, we check if the current word
  is the same as the word assigned to this char key in map
        if not, return False; else continue
- if the pattern char is not in map that we bank, assign current word as
  value of the key c

- return True if we end
"""


def word_pattern(pattern: str, s: str) -> bool:
    """
    Return if a sentence follows a pattern.

    Time: O(N) - hashing and indexing with iteration
    Space: O(N) - number of unique words in s

    :param pattern: a string, the pattern
    :param s: a sentence of words
    :return: a boolean
    """
    words = s.split(' ')
    word_map = {}
    seen = [0] * 26
    n = len(pattern)

    if len(words) != n:
        return False

    for i in range(n):
        c = ord(pattern[i]) - ord('a')
        word = words[i]
        if word not in word_map:
            if not seen[c]:
                word_map[word] = pattern[i]
                seen[c] = 1
            elif seen[c]:
                return False
        else:
            if word_map[word] != pattern[i]:
                return False
    return True
