"""
2244. Minimum Rounds to Complete All Tasks
"""


def minimum_rounds(tasks) -> int:
    """
    Return the minimum rounds required to complete all tasks of same difficulties.

    Time O(N)
    Space O(N)

    :param tasks: a list of int
    :return: an int. -1 if the tasks cannot all be completed, else the minimum rounds needed to complete tasks
    """
    task_count, ans = dict(), 0
    for task in tasks:
        task_count[task] = 1 if task not in task_count else task_count[task] + 1

    for count in task_count.values():
        if count == 1:
            return -1
        if count == 2 or count == 3:
            ans += 1
        elif count > 3:
            # if it's greater than 3 and divisible by 3, take the count
            # if there's remaining, an extra round is required to either take
            # one from the groups of 3 to have 2 remaining or to resolve 2 remaining
            ans = ans + count // 3 if count % 3 == 0 else ans + count // 3 + 1
    return ans
