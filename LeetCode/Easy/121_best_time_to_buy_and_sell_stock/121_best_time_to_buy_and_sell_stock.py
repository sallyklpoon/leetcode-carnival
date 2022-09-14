"""
Question 121: Best time to buy and sell stock
"""


def max_profit_bf(prices: list) -> int:
    """
    Return the max profit from selling stock. Brute Force Solution.

    Time-Complexity: O(N^2) time, with nested for-loops.
    Space Complexity: O(1)

    :param prices: a list of integers
    :return: an int, the max profit
    """
    prices.reverse()
    profit = 0
    for i, price in enumerate(prices):
        if price - min(prices[i:]) > profit:
            profit = price - min(prices[i:])
    return profit


def max_profit_v1(prices: list) -> int:
    """
    Return the max profit from selling stock. One-pass.

    Time-Complexity: O(N)
    Space-Complexity: O(1)

    :param prices: a list of integers
    :return: an int, the max profit
    """
    i, j = 0, 1
    min_number = float('inf')
    profit = 0
    while j < len(prices):
        if prices[i] > prices[j]:
            min_number = prices[j]
            i = j
            j = i + 1
            continue
        elif prices[i] < min_number:
            min_number = prices[i]
        curr_profit = prices[j] - prices[i]
        if curr_profit > profit:
            profit = curr_profit
        j += 1
    return profit


if __name__ == '__main__':
    print(max_profit_bf([]))
    print(max_profit_bf([4]))
    print(max_profit_bf([1, 6]))
    print(max_profit_bf([7, 1, 5, 3, 6, 4]))

    print(max_profit_v1([]))
    print(max_profit_v1([4]))
    print(max_profit_v1([1, 6]))
    print(max_profit_v1([7, 1, 5, 3, 6, 4]))
    print(max_profit_v1([2, 1, 2, 1, 0, 1, 2]))
