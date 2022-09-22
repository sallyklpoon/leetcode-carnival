"""
2269. Find the K-Beauty of a Number

The k-beauty of an int, num, is defined as the number of substrings of num when it is read as a string
that meet the following conditions:
* it has a length of k
* it is a divisor of num
Given int num and k, return the k-beauty of num
Leading zeros are allowed
0 is not a divisor of any value
"""


def divisor_substrings_bf(num: int, k: int) -> int:
    """
    Return the k-beauty of an integer given length k.

    Solution uses library methods of string conversion to int vice versa, which takes O(N)

    Time Complexity: O(N^2) - while loop with string conversion
    Space Complexity: O(1)

    :param num: an int
    :param k: an int, the length of the substrings in num
    :return: an int, the k-beauty number

    >>> divisor_substrings_bf(240, 2)
    2
    >>> divisor_substrings_bf(430043, 2)
    2
    """
    str_num = str(num)
    i, k_beauty = 0, 0

    while i + k - 1 < len(str_num):
        current_num = int(str_num[i:i + k])
        if current_num and num % current_num == 0:
            k_beauty += 1
        i += 1

    return k_beauty
