def threeConsecutiveOdds(arr: list) -> bool:
    """
    Time: O(N)
    Space: O(1)

    :param arr: array of int
    :return: a boolean
    """
    count = 0
    for num in arr:
        if num % 2 == 1:
            count += 1
        else:
            count = 0
        if count == 3:
            return True
    return False
