"""
938. Range Sum of BST

If node low <= val <= high:
add to sum
add both neighbours

If node val > high:
# we need to go lower
add left node only

If node val < low
# we need to look higher
add r node only

"""
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def range_sum_bst(root, low: int, high: int) -> int:
    """
    Iteratively sum the node values within a given low to high range.

    Time: O(N)

    :param root: a TreeNode
    :param low: an int
    :param high: an int
    :return: an int
    """
    ans, queue = 0, deque([root])
    while queue:
        curr = queue.popleft()
        if low <= curr.val <= high:
            ans += curr.val
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        elif curr.val < low and curr.right:
            queue.append(curr.right)
        elif curr.val > high and curr.left:
            queue.append(curr.left)
    return ans
