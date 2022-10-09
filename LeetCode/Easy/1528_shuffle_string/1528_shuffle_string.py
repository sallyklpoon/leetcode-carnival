"""
1528. Shuffle String

"""


def restore_string(s: str, indices: list) -> str:
    """
    Time Complexity: O(N)
    Space Complexity: O(N) - where N is the length of the string, s

    :param s: a string
    :param indices: a list of int
    :return: a string, the original s string reshuffled
    """
    result = ['' for i in range(len(s))]
    for i in range(len(s)):
        result[indices[i]] = s[i]
    return ''.join(result)


def restore_string_v1(s: str, indices: list) -> str:
    """
    Time Complexity: O(N)
    Space Complexity: O(N) - where N is the length of the string, s

    :param s: a string
    :param indices: a list of int
    :return: a string, the original s string shuffled
    """
    result = ['' for i in range(len(s))]
    for i in range(len(s)):
        result[indices[i]] = s[i]

    output = ''
    for char in result:
        output += char
    return output
