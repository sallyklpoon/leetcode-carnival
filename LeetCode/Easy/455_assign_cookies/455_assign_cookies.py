"""
455. Assign Cookies

sort the greed and size of cookies.

Iterate through both using two pointers:
When a size of cookie satisfies a child, we increment both pointers and add to count.
If size of cookies is less than greed, then we move down the greed chart for a smaller greed size.

return the count
"""


def find_content_children(g: list, s: list) -> int:
    """
    Return the maximum number of children that can be satisfied with the given
    cookies.

    Time O(NlogN) - sorting
    Space O(1)

    :param g: a list of int, the greed of children
    :param s: a list of int, the cookies and their sizes
    :return: an int, the max count of children that will be satisfied
    """
    g.sort(reverse=True)
    s.sort(reverse=True)
    count, i, j = 0, 0, 0
    while i < len(s) and j < len(g):
        if s[i] >= g[j]:
            i, j = i + 1, j + 1
            count += 1
        else:
            j = j + 1
    return count
