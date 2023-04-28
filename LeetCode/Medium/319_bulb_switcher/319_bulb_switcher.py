from math import isqrt


def bulbSwitch_bitwise(n: int) -> int:
    if n == 0: return 0
    if n == 1: return 1

    # all bulbs on and every second one off
    bulbs = [1, 0] * (n // 2)
    if n % 2 == 1:
        bulbs.append(1)
    bulbs = int(''.join(str(digit) for digit in bulbs), 2)

    if n > 2:
        for i in range(3, n):
            tog = 0
            for j in range(n - i, -1, -i):
                tog += 2 ** j
            bulbs ^= tog

        bulbs ^= 1

    count_on = 0
    while bulbs:
        count_on += bulbs & 1
        bulbs >>= 1

    return count_on


def bulbSwitch_math(n: int) -> int:
    """
    Time: O(1)
    Space: O(1)

    Consider a pattern

    1: 1
    2: 1
    3: 2
    4: 2
    5: 2
    8: 3
    :param n: an integer
    :return: an integer, the count of bulbs that are on at the end
    """
    return isqrt(n)
