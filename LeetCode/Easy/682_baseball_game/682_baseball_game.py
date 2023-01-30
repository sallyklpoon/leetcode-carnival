"""
682. Baseball Game

Stack question, we will always check before.
"""


class Solution:
    def call_points(self, operations: list) -> int:
        """
        Return the sum of call points.

        Time: O(N), N as number of operations
        Space: O(N), up to N integers from operations

        :param operations: a list of strings
        :return: an int, the sum of scores
        """
        scores = [0]  # initiate with 0 for addition index error
        for operation in operations:
            if operation.strip('-').isnumeric():
                scores.append(int(operation))
            elif operation == '+':
                added = scores[-1] + scores[-2] if len(scores) > 1 else scores[0]
                scores.append(added)
            elif operation == 'D':
                scores.append(scores[-1] * 2)
            else:
                scores.pop()
        return sum(scores)
