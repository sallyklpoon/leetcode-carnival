"""
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""


def remove_nth_from_end(head, n):
    """
    Given the head of a linked list, remove the nth node from the end of the list and return its head.

    Time: O(N), two-pass
    Space: O(1)

    :param head: Head of a linked list, where object is defined in comments above
    :param n: an int, the nth node from the end of list to remove
    :return: the head of the linked list
    """
    sz = 0
    curr_node = head
    while curr_node:
        sz += 1
        curr_node = curr_node.next

    j = sz - n + 1
    i = 1
    if i == j:
        return head.next
    curr_node = head
    while curr_node:
        if curr_node.next and i + 1 == j:
            new_next = curr_node.next.next
            curr_node.next = new_next
            break
        i += 1
        curr_node = curr_node.next
    return head
