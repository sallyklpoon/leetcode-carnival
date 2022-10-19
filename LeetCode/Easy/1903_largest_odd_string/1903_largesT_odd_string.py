"""
1903. Largest Odd Number in String

Largest number will always be the full length of the string as int.
Check if the int of the last value in the string is odd. If yes, return. Otherwise, we can keep going!

There is no necessity to shorten from the LHS because Right-most value determines if number is odd.

"22232" -> "2223"
"1342536" -> "134253"
"""


def largest_odd_number(num: str) -> str:
    """
    Return the largest odd substring in the num string.

    Time: O(N)
    Space: O(1), no extra space used

    :param num: a string of an int
    :return: a string, the largest odd substring
    """
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 == 1:
            return num[:i + 1]
    return ""
