"""
100. Same Tree

"""
from LeetCode.ds import TreeNode


def same_tree(p, q) -> bool:
    """
    Return if p and q are the same trees.

    Time O(N)
    Space O(N)

    :param p: a TreeNode, root node
    :param q: a TreeNode, root node
    :return: a bool
    """
    p_stack = [p]
    q_stack = [q]
    while p_stack:
        p_node = p_stack.pop()
        q_node = q_stack.pop()
        if p_node and p_node.val != q_node.val:
            return False
        if p_node:
            p_stack.append(p_node.left)
            q_stack.append(q_node.left)
            p_stack.append(p_node.right)
            q_stack.append(q_node.right)
    return True


if __name__ == '__main__':
    p_2 = TreeNode(2)
    p_3 = TreeNode(3)
    p = TreeNode(1, p_2, p_3)

    q_2 = TreeNode(2)
    q_3 = TreeNode(3)
    q = TreeNode(1, q_2, q_3)

    print(same_tree(p, q))
