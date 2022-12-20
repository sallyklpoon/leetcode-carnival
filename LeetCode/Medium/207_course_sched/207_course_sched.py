"""
207. Course Schedule
https://leetcode.com/problems/course-schedule/description/

We are unable to take all courses if there is a directed cycle that
exists within the graph of courses.

DFS each node to find if there exists a cycle.
- Return false if there is a cycle for any given node
- Return true if there is no cycle
"""


def can_finish(num_courses: int, prerequisites: list) -> bool:
    """
    Determine if all courses can be completed given the prerequisites.

    :param num_courses: an int
    :param prerequisites: a list of 2-indexed pairs
    :return: a boolean
    """
    adj = {i: [] for i in range(0, num_courses)}
    for prereq in prerequisites:
        adj[prereq[0]].append(prereq[1])

    for v in adj:
        visited, recStack = [False] * num_courses, [False] * num_courses
        if has_cycle(v, visited, recStack, adj):
            return False
    return True


def has_cycle(curr_node, visited, recStack, adj):
    visited[curr_node] = True
    recStack[curr_node] = True
    for neighbour in adj[curr_node]:
        if recStack[neighbour]:
            return True
        elif not visited[neighbour]:
            if has_cycle(neighbour, visited, recStack, adj):
                return True
    recStack[curr_node] = False
    return False
