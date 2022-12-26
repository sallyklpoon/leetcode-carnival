"""
232. Implement Queue using Stacks
using only two stacks.
https://leetcode.com/problems/implement-queue-using-stacks/
You must use only standard operations of a stack, which means only
- push to top,
- peek/pop from top
- size
- is empty
operations are valid.

We will use stacks to move back and forth where:
- self.stack is the main stack we will always return to
- self.queue is the stack where, when we pop from stack, we get the first element at top of the stack

-- when reading or removing anything to do with the first, we must make use of queue to switch elements
back and forth.
"""


class MyQueue:

    def __init__(self):
        self.stack = []  # where first is at i=0
        self.queue = []  # where first is last

    def push(self, x: int) -> None:
        """
        Time O(1)
        Space O(1)

        :param x: an int, an element to add to the queue
        :return: none
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Time O(N)

        :return: the popped element
        """
        while self.stack:
            e = self.stack.pop()
            self.queue.append(e)
        head = self.queue.pop()
        while self.queue:
            e = self.queue.pop()
            self.stack.append(e)
        return head

    def peek(self) -> int:
        """
        Time O(N)

        :return: the element at the front of the queue
        """
        while self.stack:
            e = self.stack.pop()
            self.queue.append(e)
        head = self.queue[-1]
        while self.queue:
            e = self.queue.pop()
            self.stack.append(e)
        return head

    def empty(self) -> bool:
        """
        O(1)

        :return: if the queue is empty
        """
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
