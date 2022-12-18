"""
49. Group Anagrams

We need to track that words that have same letters are grouped together.

I will use a hashmap, and sort each word. Matching the hashmap key which is the sorted string itself.
Append a given word if its sorted version is already in the map.

Return the map's values. Ta-da!

I've also seen in solutions discussion that a good approach may also be to create your own hashing for each word
and compare the hashing of the strings. :)
"""


def group_anagrams(strs):
    """
    Group a list of words by anagrams.

    Time: O(n log m) - m being the largest string, sorting the strings
    Space: O(n)

    :param strs: a list of strings
    :return: a 2D matrix, list of anagrams
    """
    word_map = {}

    for word in strs:
        temp = ''.join(sorted(word))
        if temp in word_map:
            word_map[temp].append(word)
        else:
            word_map[temp] = [word]
    return word_map.values()

