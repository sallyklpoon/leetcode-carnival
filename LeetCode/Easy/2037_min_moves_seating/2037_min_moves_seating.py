"""
2037. Minimum Number of Moves to Seat Everyone
"""


def min_moves_to_seat(seats: list, students: list) -> int:
    """
    Return the number of moves to have each student in a seat.

    Time Complexity: O(N log N) - Python uses combo of Quicksort and Merge Sort
    Space Complexity: O(1) - output only

    :param seats: list of int
    :param students: list of int
    :return: int, number of moves
    """
    seats.sort()
    students.sort()

    moves = 0
    for i in range(len(seats)):
        moves += abs(seats[i] - students[i])
    return moves
