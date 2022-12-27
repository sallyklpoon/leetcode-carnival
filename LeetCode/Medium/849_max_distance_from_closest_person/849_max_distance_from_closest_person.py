"""
849. Maximize Distance to Closest Person
https://leetcode.com/problems/maximize-distance-to-closest-person/

Notes:
- For Alex to have max seating between himself and another person, he must
always sit in the centre between two people or, if no person is at seat 0.
- The max from first closest person will always be the first index of a seated person
- The max away from last person will always be number of seats - last index

Approach:
- Find the seats that are taken
- dp problem
- Max distance from first person is the first index of 1
- Max distance between two people is second seat num - first seat num divided by 2
- Max distance from last person is the end of list - i
"""


def max_dist_to_closest(seats: list) -> int:
    """
    Return the maximum distance between the closest person.

    Time: O(N)
    Space: O(1)

    :param seats: a list of int
    :return: an int
    """
    max_seats = 0
    n = len(seats)
    i, j = 0, 0
    # check for first seated
    while j < n:
        if seats[i] == 0:
            i, j = i + 1, j + 1
        else:
            max_seats = i
            break
    j += 1
    # check middle
    while j < n:
        if seats[j]:
            distance = (j - i) // 2
            max_seats = distance if distance > max_seats else max_seats
            i = j
        j += 1
    # check last seated
    max_seats = n - 1 - i if (n - 1 - i) > max_seats else max_seats

    return max_seats
