"""
150. Evaluate Reverse Polish Notation

TIL
eval() in Python can execute a given string as Python
int() rounds towards 0, whereas // will round down always
"""

OPERATION = {
    '*': lambda a, b: a * b,
    '-': lambda a, b: a - b,
    '+': lambda a, b: a + b,
    '/': lambda a, b: int(a / b)
}


def eval_rpn(tokens) -> int:
    """
    Solve a given list of RPN tokens.

    Stack solution

    Time: O(N)
    Space: O(N - 1) up to how many tokens there may be

    :param tokens: a list of strings
    :return: an integer
    """
    s = []
    for e in tokens:
        if e.lstrip('-').isdigit():
            s.append(int(e))
        else:
            b = s.pop()
            a = s.pop()
            s.append(OPERATION[e](a, b))    # can also do eval(f"{a}{e}{b}")
    return s.pop()

