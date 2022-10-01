"""
1572. Matrix Diagonal Sum

             i, j
[1, 2, 3, x] 0, -1
[4, 5, 6, x] 1, -2 <-- 4 - 2 = 2
[7, x, x, 4] 2, -3 <-- 4 - 3 = 1
[1, 1, 1, 3] 3, -4

          i, j
[1, 2, 3] 0, -1
[4, 5, 6] 1, -2 <-- 3 - 2 = 1 if they are equal, we only add one of them for odd
[7, 8, 9] 2, -3

"""


def diagonal_sum(mat: list) -> int:
    """
    Return the sum of the matrix diagonals, given a matrix of integers.

    Time Complexity: O(N) - iterate through each array (performed > 99.7%)
    Space Complexity: O(1) - store single number indexes

    :param mat: list of lists containing integers
    :return: an int, the sum of the diagonal values in the matrix
    """
    i, j = 0, -1
    sum_output = 0
    for in_mat in mat:
        sum_output += in_mat[i] + in_mat[j]
        if i == len(mat) + j:
            sum_output -= in_mat[j]
        i, j = i + 1, j - 1
    return sum_output
