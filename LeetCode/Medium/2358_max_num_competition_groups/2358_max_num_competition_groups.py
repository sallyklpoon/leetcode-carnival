"""
2358. Maximum Number of Groups Entering a Competition

Split a group of students with grades into groups

- Each group must have lower sum and lower count of students than group after it
- return the maximum number of groups that we can form

- track remaining students to sort
- track size of group, starting with 1 and ++ by 1 each time.
- assume if we sort the grades, we will always be able to divide up groups according to first req of sums

- use a loop to check if the remaining students to sort is >= size
    - if yes, we can create a new group
    - if no, we append remaining to the last group

- return the count
"""
from typing import List


def maximum_groups(grades: List[int]) -> int:
    rem_students = len(grades)
    size, count = 1, 0

    while rem_students >= size:
        rem_students -= size
        size, count = size + 1, count + 1

    return count
