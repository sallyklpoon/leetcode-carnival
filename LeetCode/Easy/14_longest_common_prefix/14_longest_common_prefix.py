"""
14. Longest Common Prefix

strs = ["flower", "flow", "flight"]
returns "fl"

The shortest word is the max length that the prefix will be.
- sort list to find the shortest word at index 0 O(n log n) -- quick sort and merge sort combo in python

"""


def longest_common_prefix_bf(strs: list) -> str:
    """
    Return the longest common prefix in a list of words.

    Time Complexity: O(NM) nested loop where N is length of shortest string, M is num of stringsgit add
    Space Complexity: O(1)

    :param strs: a list of strings
    :return: a string, the longest common prefix

    >>> longest_common_prefix_bf(["flower", "flow", "flight"])
    'fl'
    >>> longest_common_prefix_bf([])
    ''
    >>> longest_common_prefix_bf(["a"])
    'a'
    >>> longest_common_prefix_bf([""])
    ''
    >>> longest_common_prefix_bf(["dog", "racecar", "car"])
    ''
    """
    prefix = ""
    flag = False

    if not strs:
        return prefix

    strs.sort(key=len)
    for i in range(len(strs[0])):
        for word in range(len(strs)):
            if strs[word][i] != strs[0][i]:
                flag = True
        if flag:
            return prefix
        prefix += strs[0][i]

    return prefix




