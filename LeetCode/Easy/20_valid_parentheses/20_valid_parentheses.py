"""
20. Valid Parentheses

[{(

]})
"""


def is_valid(s: str) -> bool:
    """
    Determine if a given string of parentheses is valid.

    Time Complexity: O(N) - use of hashing to validate key and indexes in list.
    Space Complexity: O(N) - store of stack

    :param s: string of brackets
    :precondition: String only contains parentheses characters
    :return: boolean, True if the string has valid parentheses order

    >>> is_valid("()")
    True
    >>> is_valid("()[]{}")
    True
    >>> is_valid("(]")
    False
    >>> is_valid("((")
    False
    >>> is_valid(")(){}")
    False
    >>> is_valid("))")
    False
    """
    brackets = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    stack = []

    for i in range(len(s)):
        curr_char = s[i]

        if stack:
            if curr_char in brackets.keys():
                stack.append(curr_char)
            elif curr_char == brackets[stack[-1]]:
                stack.pop()
            else:
                return False
        else:
            if curr_char not in brackets.keys():
                return False
            stack.append(curr_char)

    return not stack

