"""
806. Number of Lines To Write String
"""


def num_of_lines(widths: list, s: str) -> list:
    """
    Return the lines and final line width given a string and each character's pixel width.

    Time: O(N)
    Space: O(1)

    :param widths: a list of widths per 26 alphabet chars
    :param s: a string of lowercase English letters
    :return: a list, [the total num of lines, the width of the last line in pixels]
    """
    curr_len = 100
    lines = 1
    for word in s:
        width = widths[ord(word) - 97]
        if curr_len - width < 0:
            curr_len = 100
            lines += 1
        curr_len -= width

    return [lines, 100 - curr_len]
