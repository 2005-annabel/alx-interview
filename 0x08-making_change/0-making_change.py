#!/usr/bin/python3
'''Given a pile of coins of different values,
    determine the fewest number of coins needed to meet
    a given amount total.
'''
import sys

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list of int): The values of the coins in your possession.
        total (int): The total amount to meet.

    Returns:
        int: The fewest number of coins needed to meet the total, or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    # Initialize the dp array with a value greater than the possible number of coins needed
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
