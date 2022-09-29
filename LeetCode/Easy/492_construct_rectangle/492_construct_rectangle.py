"""
492. Construct the Rectangle
"""
import math


def construct_rectangle(area: int) -> list:
    """
    Construct a rectangle with the minimum difference between length and width.

    Time Complexity - O(N), however, time limit exceeded in LC runtime
    Space Complexity - O(1)

    :param area: int
    :return: list of int, the width and length dimensions
    """
    output, ratio = [0, 0], area

    for i in range(1, area + 1):
        dividend = area // i
        if area % i == 0 and abs(i - dividend) < ratio:
            output = [dividend, i]
            ratio = abs(i - dividend)

    return output


def construct_rectangle_math(area: int) -> list:
    width = int(math.sqrt(area))
    while area % width != 0:
        width -=1
    return [area//width, width]
