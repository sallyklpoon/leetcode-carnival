"""
1075. Number Of Rectangles That Can Form The Largest Square

HashMap approach
- store count of the min of each set of rectangle value
- we return the value from the key in this map that is the largest
---> space = O(N)
---> Time = O(N) - although max() function or finding largest val between each
     rectangle is O(N) time, each rectangle is only 2 elements, constant. No variance.

If we want to use less space, I can foresee a two-pass method
- first pass, we store the max_square_width
- each rect we approach, we get the min value of the pair and check if it's created than max_square_width.
Update if yes.
- second pass, we can filter the list for only those pairs with the max_square_width contained
- return the length of that list
- alternatively, we can use a simple count variable to store the count and pass through the list

-----

Correction, we can do a one-pass using the second approach too!
Since, we will always have the max_width overrode, there is no reason that this value will change.
If it changes, then count starts at one again.
"""


def count_good_rectangles(rectangles: list) -> int:
    """
    Return the count of the largest square that can be obtained in a given list of rectangles.

    Time: O(N) - although min() is O(N), each rectangle pair is constant at size 2
    Space: O(N) - worst case

    :param rectangles: a list of int lists of len 2
    :return: an int
    """
    min_counts = dict()

    for rectangle in rectangles:
        min_width = min(rectangle)
        min_counts[min_width] = 1 if min_width not in min_counts else min_counts.get(min_width) + 1

    return min_counts[max(min_counts)]


def count_good_rectangles_less_space(rectangles: list) -> int:
    """
    Return the count of the largest square that can be obtained in a given list of rectangles.

    Time: O(N)
    Space: O(1)

    :param rectangles: a list of int lists of len 2
    :return: an int
    """
    count, max_side = 0, 0

    for length, width in rectangles:
        small_side = min(length, width)
        if small_side > max_side:
            count, max_side = 1, small_side
        elif small_side == max_side:
            count += 1

    return count
