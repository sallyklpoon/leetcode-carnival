"""
1472. Design Browser History
https://leetcode.com/problems/design-browser-history/description/

- keep array of urls
- have a pointer

-----
Later optimization.

To keep visit at O(1), we can keep an extra count for the actual number
of history we have. This may waste space, but it will operate at a faster time.

Initially, I had implemented with slicing the history list and appending.
"""


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.pointer = 0
        self.count = 1

    def visit(self, url: str) -> None:
        """
        Visit a given url, clear forward history.

        Time: O(1)
        Space: O(1)

        :param url: a string
        :return: None
        """
        if self.count == len(self.history) and self.pointer == self.count - 1:
            self.history.append(url)
        else:
            self.history[self.pointer + 1] = url
        self.pointer += 1
        self.count = self.pointer + 1

    def back(self, steps: int) -> str:
        """
        Move back number of steps.
        If steps is greater than x, where x is max steps, move x steps.

        Time: O(1)
        Space: O(1)

        :param steps: an int, number of steps
        :return: a string, the url of the current page
        """
        steps = self.pointer if steps > self.pointer else steps
        self.pointer -= steps
        return self.history[self.pointer]

    def forward(self, steps: int) -> str:
        """
        Move forward number of steps.
        If steps is greater than x, where x is max steps, move x steps.

        Time: O(1)
        Space: O(1)

        :param steps: an int, number of steps
        :return: a string, the url of the current page
        """
        max_steps = self.count - 1 - self.pointer
        steps = max_steps if steps > max_steps else steps
        self.pointer += steps
        return self.history[self.pointer]
