# Solving the Coin Change Problem

The Coin Change Problem is a classic algorithmic problem in computer science and mathematics. Given a pile of coins of different values, the goal is to determine the fewest number of coins needed to meet a given amount total. In this README, we'll discuss how to solve this problem using Python.

## Problem Statement

The problem can be summarized as follows:

- **Input:** You are given a list of coin denominations (`coins`) and a target total (`total`).
- **Output:** Find the fewest number of coins needed to meet the target total.

## Solution Approach

We can approach this problem using a dynamic programming technique, specifically, the "coin change" dynamic programming approach. The idea is to build a table where each cell `(i, j)` represents the minimum number of coins needed to make the total `j` using the first `i` coin denominations.

Here are the steps to solve the problem:

1. Create an array `dp` of length `total + 1` and initialize all values to a large number (e.g., `float('inf')`).

2. Set `dp[0]` to 0 because it takes zero coins to make a total of 0.

3. Iterate through each coin denomination in the `coins` list.

4. For each coin denomination `coin`, iterate through the `dp` array from `coin` to `total`.

5. Update `dp[j]` to the minimum between its current value and `dp[j - coin] + 1`. This step calculates the minimum number of coins needed to make the total `j` using the current coin denomination.

6. After processing all coin denominations, the value at `dp[total]` will represent the minimum number of coins needed to make the target total. If it remains equal to the initial large number, it means the target total cannot be met, so return -1.

7. Otherwise, return the value at `dp[total]`.

## Example Usage

```python
from typing import List

def makeChange(coins: List[int], total: int) -> int:
    if total < 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for j in range(coin, total + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1
```

## Example

Let's demonstrate the usage of the `makeChange` function with an example:

```python
coins = [1, 2, 5]
total = 11
result = makeChange(coins, total)
print(result)  # Output: 3 (11 = 5 + 5 + 1)
```

## Time Complexity

The time complexity of this solution is O(total * n), where `n` is the number of coin denominations and `total` is the target total. The space complexity is O(total).

This README provides an overview of how to solve the Coin Change Problem using dynamic programming. You can use the provided `makeChange` function to find the fewest number of coins needed to meet a given amount total for different sets of coin denominations and target totals.