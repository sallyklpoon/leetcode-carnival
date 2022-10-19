"""
692. Top K Frequent Words
"""


def top_k_frequent(words: list, k: int) -> list:
    """
    Return a list of k most frequent strings.

    Time: O(N log N)
    Space: O(N)

    :param words: a list of strings
    :param k: an int
    :return: a list of strings
    """
    count = dict()
    for word in words:
        count[word] = 1 if word not in count.keys() else count[word] + 1

    output = list(zip(count.keys(), count.values()))
    output.sort(key=lambda x: (-x[1], x))
    output = [output[i][0] for i in range(k)]
    return output
