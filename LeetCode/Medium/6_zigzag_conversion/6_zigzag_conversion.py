"""
6. Zigzag Conversion

Convert a string into zigzag version given a certain number of rows.

Use a row counter, which will increase going down until we reach the max number of rows.
Decrease until we reach row 1, then increase again.

Aggregate the string and return.

DS: map
"""


def convert(s: str, numRows: int) -> str:
    """
    Convert a string into its zigzag format.

    Time: O(M) - M characters in the string
    Space: O(N) - N rows

    :param s: a string
    :param numRows: an int, the number of rows
    :return: the converted string
    """
    if numRows == 1:
        return s

    row_num, i, inc = 1, 0, True
    n = numRows + 1
    rows = {k: "" for k in range(1, n)}

    for c in s:
        rows[row_num] += c
        if inc:
            row_num += 1
            if row_num == numRows:
                inc = False
        else:
            row_num -= 1
            if row_num == 1:
                inc = True

    ans = ""
    for j in range(1, n):
        ans += rows[j]

    return ans
