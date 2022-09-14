"""
Question 121: Best time to buy and sell stock
"""


def max_profit_bf(prices: list) -> int:
    """
    Return the max profit from selling stock. Brute Force Solution.

    This algorithm runs at O(N^2) time, with nested for-loops.
    The space complexity is O(1) constant time.

    :param prices: a list of integers
    :return: an int, the max profit
    """
    prices.reverse()
    profit = 0
    for i, price in enumerate(prices):
        if price - min(prices[i:]) > profit:
            profit = price - min(prices[i:])
    return profit


if __name__ == '__main__':
    print(max_profit_bf([]))
    print(max_profit_bf([4]))
    print(max_profit_bf([1, 6]))
    print(max_profit_bf([7, 1, 5, 3, 6, 4]))

