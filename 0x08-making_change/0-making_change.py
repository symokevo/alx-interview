#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """
    make change
    """
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for i in range(len(coins)):
        for j in range(coins[i], total + 1):
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)
    if dp[total] != float('inf'):
        return dp[total]
    else:
        return -1
