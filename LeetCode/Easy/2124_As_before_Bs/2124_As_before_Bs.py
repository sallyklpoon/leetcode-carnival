"""
2124. Check if All A's Appears Before B's

Two possible approaches:

1-pass
- use bool flag
- iterate through the list, flag when b
- after flag, if a occurs again, return false
- otherwise, return true

1-pass, two pointers (maybe quicker?)
- one starts at front 0...n-1
- another starts at back -1
- back flags when b becomes a and if there is occurrence of B, return false
- front flags when a becomes b and if there is occurrence of A, return false
- stop and return true when front index >= len + back index or

[4, 3, 2, 1]
0. 1  2  3
-4 -3 -2 -1

"""


def check_string_v1(s: str) -> bool:
    flag = False
    for letter in s:
        if not flag and letter == 'b':
            flag = True
        if flag and letter == 'a':
            return False
    return True
