"""
2319. Check if Matrix is X-Matrix
"""


def check_x_matrix(grid: list) -> bool:
    """
    Determine if the given matrix is an x-matrix.

    Time Complexity: O(N^2) - a matrix search
    Space Complexity: O(1) - store pointers

    :param grid: a list of integer lists
    :return: boolean
    """
    # track pointer for expected > 0 value squares per row
    i, j = 0, len(grid) - 1

    for row in grid:
        for index in range(len(grid)):
            if index == i and not row[i] or index == j and not row[j]:
                return False
            elif index != i and index != j:
                if row[index]:
                    return False
        i, j = i + 1, j - 1     # move pointer

    return True
