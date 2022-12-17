"""
931. Minimum Falling Path Sum

Backtracking?
For every col in the first row, we solve for the smallest falling path sum.
Store the min sum each time we complete a full fall path with min sum
Aside from the first row val, we should always select the smallest number


I may need every single path to compare as min_sum
Recursive strategy?

Get the most min sum on each row and then take the minimum of the final row.

Needed help on this one!
https://leetcode.com/problems/minimum-falling-path-sum/solutions/186646/the-art-of-dynamic-programming/
"""


def min_falling_path_sum(matrix) -> int:
    row, col = len(matrix), len(matrix[0])
    for i in range(1, row):
        for j in range(col):
            a = matrix[i - 1][j - 1] if j > 0 else float('inf')
            b = matrix[i - 1][j]
            c = matrix[i - 1][j + 1] if j < col - 1 else float('inf')
            matrix[i][j] += min(a, b, c)
    return min(matrix[-1])
