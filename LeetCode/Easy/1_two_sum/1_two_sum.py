def two_sum_bf(nums: list, target:int) -> list:
    """
    Find the index of two int resulting in the target sum.

    This solution is considered brute force as there are two implicit loops nested within each other.
    While-loop runs at O(N-1) at worse case and the Python *in* operator conducts a list search,
    which should be O(N) worse case.
    List append at O(1)

    :param nums: a list of int
    :param target: an int, the target sum
    :return: a list of int, indexes of the sum nums
    """
    output = []
    index = 0
    while len(output) == 0:
        difference = target - nums[index]
        if difference in nums[index + 1:]:
            output.append(index)
            output.append(nums[index + 1:].index(difference) + index + 1)
        index += 1
    return output


def two_sum_v2(nums: list, target:int) -> list:
    """ WIP -- incomplete solution atm, testing edge cases.

    :param nums:
    :param target:
    :return:
    """
    differences = [target - num for num in nums]    # O(N)
    possible_addends = list(set(nums).intersection(differences))
    return [nums.index(possible_addends[0]), nums.index(possible_addends[1])]



if __name__ == '__main__':
    print(two_sum_bf([3, 0, 3], 6))
    print(two_sum_v2([8, 4, 2], 6))
