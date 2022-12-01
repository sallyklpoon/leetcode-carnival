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

===== Stack Strat
stack = [de]

if curr != stack top:
   add to stack
if equal to stack

"""


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


