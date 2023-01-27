"""
206. Reverse Linked List

Three pointers to track previous, current, and next
The previous is the reversed.

At each loop, while we still have a next:
   - assign the current's next as the previous (reversed portion)
   - advance the previous pointer to include the current's head (which is not included in reverse)
   - advance the current counter to the next node, now unattached to the previous node
   - advance the next pointer to the next's next
Since we will end when there is no next, we must set the current node's next to the complete
reversed list before returning it.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def reverse_list_iterative(head):
    """
    Reverse a linked list.

    Time: O(N)
    Space: O(1)

    :param head: a linked list node or None
    :return: the reversed linked list
    """
    if not head:
        return None
    prev, curr, next_n = None, head, head.next

    while next_n:
        curr.next = prev
        prev = curr
        curr = next_n
        next_n = next_n.next

    curr.next = prev
    return curr
