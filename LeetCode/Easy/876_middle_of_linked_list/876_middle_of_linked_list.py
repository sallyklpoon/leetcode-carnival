"""
[1, 2, 3, 4, 5]
-------x--------y

[1, 2, 3, 4, 5, 6, 7, 8]
----------x-----------y

Slow and fast pointer.
If we increment y by 2 each time,
it will always be at the end vs x once every time, it will be the half point.
- We check until y hits None and return x.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def middle_node(head):
    x, y = head, head.next
    while y:
        x = x.next
        y = y.next.next if y.next else None
    return x
