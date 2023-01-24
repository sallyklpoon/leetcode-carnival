"""
160. Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists

Brute Force:
- we can check the first list and store all the addresses in a dict (for O(1) time access w/ hashing)
- then iterate through second list, checking if the node has been seen in the first list
- the first node that is in the second list and seen in first is the connecting point


"""


def get_intersection_node(headA, headB):
    """
    Return the intersection of two singly linked lists, if none, return None

    Time: O(m + n)
    Space: O(1)

    :param headA: a linked list node
    :param headB: a linked list node
    :return: an optional node
    """
    def get_size_last(head):
        size, last = 0, None
        while head:
            size += 1
            last = head if not head.next else None
            head = head.next
        return size, last

    sizeA, lastA = get_size_last(headA)
    sizeB, lastB = get_size_last(headB)
    if lastB == lastA:
        longer, size_count = (headA, sizeA) if sizeA > sizeB else (headB, sizeB)
        small, small_size = (headB, sizeB) if sizeA > sizeB else (headA, sizeA)
        while size_count != small_size:
            size_count -= 1
            longer = longer.next
        while small and longer:
            if small == longer:
                return small
            small, longer = small.next, longer.next
    return None


def get_intersection_node_hashing(headA, headB):
    """
    Return the intersecting node if it exists, otherwise None.

    Time: O(M + N)
    Space: O(M)

    :param headA: a linked list node
    :param headB: a linked list node
    :return: a node if there's an intersection, otherwise None
    """
    seen = {}
    while headA:
        seen[headA] = True
        headA = headA.next

    while headB:
        if headB in seen:
            return headB
        headB = headB.next

    return None


