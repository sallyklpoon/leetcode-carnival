"""
875. Koko Eating Bananas
https://leetcode.com/problems/koko-eating-bananas/
"""
import math


def min_eating_speed_bs(piles: list, h: int) -> int:
    """
    Return the minimum integer k where Koko can eat all bananas within h hours.

    Time: O(n log n) - binary search
    Space: O(N) - for N piles of bananas

    Approach makes use of binary search to reduce the search time for the correct speed.
    - If the time to consume all piles at a given speed is greater than h, we search for a faster speed
    - If the time to consume all piles at a given speed is less than or equal to the hour,
     ----> store the current speed if it's lower than the previous answer
     ----> continue searching a lower speed
     When search is complete, we return the answer

    :param piles: a list of integers
    :param h: an int, the hours given to consume all piles of bananas
    :return: an int, the speed, k, at which Koko should eat bananas per hour
    """
    low, high = 1, max(piles)
    ans = float('inf')
    while low <= high:
        mid = low + (high - low) // 2
        time = sum([math.ceil(piles[i] / mid) for i in range(len(piles))])
        if time > h:
            low = mid + 1
        elif time <= h:
            high = mid - 1
            if mid < ans:
                ans = mid
    return ans


def min_eating_speed_bf(piles: list, h: int) -> int:
    n = len(piles)
    if h == n:
        return max(piles)
    k = max(piles) if h < n else 1
    ans = False
    while not ans:
        time = {i: math.ceil(piles[i] / k) for i in range(len(piles))}
        if sum(time.values()) == h:
            ans = True
        else:
            k += 1
    return k
