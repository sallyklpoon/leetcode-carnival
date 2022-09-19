"""
1700. Number of Students Unable to Eat Lunch
"""


def count_students_bf(students: list, sandwiches: list) -> int:
    """
    Return the count of students who are unable to eat.

    Time Complexity:

    :param students: a list of int containing 1 or 0
    :param sandwiches: a list of int containing 1 or 0
    :return: an int

    >>> count_students_bf([1, 1, 0, 0], [0, 1, 0, 1])
    0
    >>> count_students_bf([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1])
    3
    >>> count_students_bf([1], [0])
    1
    """
    sandwich_i = 0

    while sandwich_i < len(sandwiches):
        if sandwiches[sandwich_i] in students:
            student_i = students.index(sandwiches[sandwich_i])
            del students[student_i]
            sandwich_i += 1
        else:
            return len(students)
    return len(students)


if __name__ == '__main__':
    print(count_students_bf([1, 1, 0, 0], [0, 1, 0, 1]))

