"""
1209. Remove All Adjacent Duplicates in String II

===== Recursive Strat
k = 3

deeedbbcccbdaa
---^
start_i, current_count = 1
curr = e
count = 3

str = s[:start_i] + s[start+i + count:] -> dbbcccbdaa

for every iteration of remove duplicates, we will keep iterating until

===== Stack Strat (naive)
stack = [ddbbbdaa]

count = 1
if curr != stack top:
   add to stack
   count = 1 <-- reset to 1
if equal to stack top:
   count += 1
if count == k:
   stack.pop()

if len(stack) != s_original:
   repeat the above steps

set s = stack string

check  if changed, if it's changed from original string length, we will keep removing


[ddbbbdaa]
c = 2
k = 3
"""


def remove_duplicates_stack(s: str, k: int) -> str:
    """
    Remove duplicates of k-length until none, O(N), optimized to use stack of tuples.
    Teach tuple represents the previous character and the consecutive count.

    Time: O(N)
    Space: O(N)

    :param s: a string
    :param k: an integer
    :return: a string
    """
    stack = []
    for char in s:
        if not stack or char != stack[-1][0]:
            stack.append((char, 1))
        else:
            if char == stack[-1][0]:
                stack[-1] = (char, stack[-1][1] + 1)
                if stack[-1][1] == k:
                    stack.pop()
    return ''.join([char[0] * char[1] for char in stack])


def remove_duplicates_stack_naive(s: str, k: int) -> str:
    """
    Remove duplicates of k-length until none.

    Time = O(n^2) worst time, as it reiterates through each time there's a change
    Space = O(n)

    This solution has good space complexity, but poor time complexity

    :param s: a string
    :param k: an int
    :return: a string
    """
    changed = True
    while changed:
        stack = []
        adj_count = 1
        for char in s:
            if not stack:
                stack.append(char)
                continue
            else:
                if char == stack[-1]:
                    adj_count += 1
                    if adj_count == k:
                        stack = stack[:-(k - 1)]
                        adj_count = 1
                        continue
                elif char != stack[-1]:
                    adj_count = 1
                stack.append(char)
        changed = not len(stack) == len(s)
        s = stack
    return ''.join(s)


def remove_duplicates(s: str, k: int) -> str:
    """
    Remove duplicates of k-length until none.

    Time: Recursive solution -- Time limit exceeded LC
    Space: O(1)

    :param s: a string
    :param k: an int
    :return: a string

    >>> remove_duplicates("deeedbbcccbdaa", 3)
    'aa'
    >>> remove_duplicates("abcd", 2)
    'abcd'
    """
    i, j = 0, 0
    curr = s[i]
    count = 0

    while i < len(s):
        if s[i] == curr:
            count += 1
        else:
            curr = s[i]
            j = i
            count = 1
        if count == k:
            new_str = s[:j] + s[j + count:]
            return remove_duplicates(new_str, k)
        i += 1
    return s


