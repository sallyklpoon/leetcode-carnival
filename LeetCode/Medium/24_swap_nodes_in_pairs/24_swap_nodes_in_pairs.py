class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    if not head or not head.next:
        return head

    # list must have at least 2 nodes
    head = ListNode(next=head)
    a, b, c = head, head.next, head.next.next

    while c:
        tail = c.next
        b.next = tail
        c.next = b
        a.next = c
        a, b = b, b.next
        c = b.next if b else None

    return head


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
swapPairs(a)