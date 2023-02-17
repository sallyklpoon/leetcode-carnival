from collections import deque


def longest_palindrome(s: str) -> str:
    n = len(s)
    if n < 2:
        return s

    longest, temp = s[0], deque(s[1])
    i = 1
    j, k = i - 1, i + 1
    for i in range(1, n - 2):
        if 0 <= j == k < n:
            temp.appendleft(s[j])
            temp.append(s[k])
            j -= 1
            k += 1
        else:
            i += 1
            j, k = i - 1, i + 1
            longest = "".join(temp) if len(temp) > len(longest) else longest
            temp = deque(s[i])

    return longest


print(longest_palindrome("bbabad"))