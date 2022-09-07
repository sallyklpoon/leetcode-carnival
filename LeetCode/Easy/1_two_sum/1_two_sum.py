def two_sum_bf(nums:list, target:int) -> list:
    """
    Find the index of two int resulting in the target sum.

    This solution is considered brute force as there are two implicit loops nested within each other.
    While-loop runs at O(N-1) at worse case and the Python *in* operator conducts a list search,
    which should be O(N) worse case
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
            return [index, nums[index + 1:].index(difference) + index + 1]
        index += 1

 def two_sum_v2(nums:list, target:int) -> list:
     """
     Find the index of two int resulting in the target sum

     This solution will work at O(N) time. It goes through the list of nums once, storing the index
     and value in the hashmap, and checks if its difference addend exists already in the hashmap keys.
     Finding a hash key is at O(1) time

    :param nums: a list of int
    :param target: an int, the target sum
    :return: a list of int, indexes of the sum nums
     """
     i_map = {}
     for i, num in enumerate(nums):
         if target - num in i_map.keys():
             return [i, i_map[target - num]]
         i_map[num] = i


if __name__ == '__main__':
    print(two_sum_bf([3, 0, 3], 6))
    print(two_sum_v2([8, 4, 2], 6))
