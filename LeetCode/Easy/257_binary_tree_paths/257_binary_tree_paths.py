"""
257. Binary Tree Paths

DFS, each side, we will form our given string by searching left and right
A leaf node is one that does not have left or right nodes. We can append it to our ans.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def binaryTreePaths(root) -> list:
    ans = []

    def dfs(node, path):
        if path != "":
            path += "->"
        path += str(node.val)
        if not node.left and not node.right:
            ans.append(path)
        if node.left:
            dfs(node.left, path)
        if node.right:
            dfs(node.right, path)

    dfs(root, "")
    return ans
