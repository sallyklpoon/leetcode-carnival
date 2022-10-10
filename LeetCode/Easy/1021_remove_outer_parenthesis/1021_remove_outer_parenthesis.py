"""
(()())(())

[()]

"()()()"

((())())(())(()(()))


[((())())]
[01111110]

every time we meet a closing ')' parenthesis to match with the current top of stack,
if the size of stack is > 2, then we can append this popped parenthesis off!

"""


def remove_outer_parentheses(s: str) -> str:
    """
    Return a string with outer parenthesis removed.

    Time Complexity: 2 * O(N), or O(N) -- two pass
    Space Complexity: O(N) - where N is for a second array as a marker of parenthesis that shall remain
    in the output string

    :param s: a valid parenthesis string
    :return: a string with outer parenthesis removed
    """
    stack = []
    marker = [0 for i in range(len(s))]

    # First pass, find the valid parenthesis that are not outer
    for i in range(len(s)):
        char = s[i]
        if char == ')':
            marker[i] = 1 if len(stack) > 1 else 0
            stack.pop()
        elif char == '(':
            marker[i] = 1 if len(stack) else 0
            stack.append(char)

    # Second pass through markers, append only the parenthesis marked
    output = ''
    for j in range(len(marker)):
        if marker[j]:
            output += s[j]

    return output
