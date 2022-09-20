"""
27. Remove Element

nums = [2, 2, -3, -3]
      -^
val = 3

first pass, mark the persistence of val
second pass, swap non-val nums to first occurrences of val

nums = [0,1,2,2,3,0,4,2]
val = 2

first pass: [0,1,-2,-2,3,0,4,-2]
second pass: [0,1,3,-2,-1,0,4,-2]
                    ^       *
"""


def remove_element(nums: list, val: int) -> int:
    """
    Remove an integer element within a list in place, return the numbers remaining in list after removal.

    Time Complexity: O(N) - 3x loops
    Space Complexity: O(1) - removal and sort in place

    :param nums: a list of int
    :param val: an int, the integer to remove from a list of integers
    :return: an int, the number of ints that are not the given val

    >>> remove_element([], 3)
    0
    >>> remove_element([3, 2, 2, 3], 3)
    2
    >>> remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2)
    5

    """
    if not nums:
        return 0

    # sort the list
    front_i = 0
    back_i = -1
    while front_i != len(nums) + back_i:    # stop when indexes meet
        if nums[front_i] != val:
            front_i += 1
        elif nums[front_i] == val:
            if nums[back_i] != val:
                nums[front_i], nums[back_i] = nums[back_i], nums[front_i]
            else:
                back_i -= 1

    # count the non-val numbers and return
    output = 0
    for i in range(len(nums)):
        if nums[i] != val:
            output += 1
        else:
            return output
