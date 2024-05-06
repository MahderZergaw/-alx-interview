#!/usr/bin/python3
"""
To  determine the fewest number of coins needed to meet a
given amount total.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet
    the given total.

    Args:
        coins (list[int]): List of coin denominations.
        total (int): Target value to achieve.

    Returns:
        int: Fewest number of coins needed to meet the total.
            If total is 0 or less, returns 0.
            If total cannot be met by any number of coins, returns -1.
    """
    if total <= 0:
        return 0

# Initialize an array to store the minimum number of coins
# for each value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
