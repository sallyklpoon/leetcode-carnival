"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters

When we are gathering a substring, we can continue appending to our longest
sub string, until we hit a char that has already appeared.
- use an array to mark the seen chars -- except we can also have symbols and digits :(, so let's use dict
- if any char count has already been seen, we start all over again with appending our substring
   we also need to update our dict for the most recent seen index
"""


def length_of_longest_substring(s: str) -> int:
    """
    Return the length of the longest substring with no repeats.

    Time O(N)
    Space: O(1) - limited characters in dict that does not go over unique characters

    :param s: a string
    :return: an int, the longest substring length
    """
    seen = dict()
    i, longest, curr = 0, 0, 0
    while i < len(s):
        char = s[i]
        if char not in seen:
            seen[char] = i
            curr += 1
        else:
            if seen[char] >= i - curr:
                longest = curr if curr > longest else longest
                curr = i - seen[char]
            else:
                curr += 1
            seen[char] = i
        i += 1
    return longest if longest > curr else curr
