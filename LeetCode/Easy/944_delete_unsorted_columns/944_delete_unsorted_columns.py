"""
944. Delete Columns to Make Sorted
https://leetcode.com/problems/delete-columns-to-make-sorted/
"""


def min_deletion_size(strs: list) -> int:
    """
    Return the minimum deletion size of unsorted columns.

    Time O(N^2)
    Space O(N) -- can be reduced to O(1) by only checking the char before in the column.

    :param strs: a list of strings of the same length
    :return: an int, the number of columns to delete
    """
    cols = len(strs[0])
    col_map = {i: [] for i in range(cols)}

    ans = 0
    for word in strs:
        for j in range(cols):
            if j in col_map:
                curr_ord = ord(word[j])
                if col_map[j] and curr_ord < col_map[j][-1]:
                    ans += 1
                    col_map.pop(j)
                else:
                    col_map[j].append(curr_ord)
    return ans
