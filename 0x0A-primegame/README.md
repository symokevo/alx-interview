# Maria vs. Ben Prime Number Game

Maria and Ben are playing a game where they take turns choosing prime numbers from a set of consecutive integers starting from 1 up to and including n. The player who cannot make a move loses the game. They play x rounds of this game, with different values of n for each round. Assuming Maria always goes first and both players play optimally, this README explains how to determine the winner of each round and find the player who won the most rounds.

## Table of Contents
- [Problem Description](#problem-description)
- [Function Prototype](#function-prototype)
- [Example](#example)
- [Implementation](#implementation)
- [How to Run](#how-to-run)
- [Contributing](#contributing)
- [License](#license)

## Problem Description

Maria and Ben play x rounds of the prime number game. In each round, they have a set of consecutive integers from 1 up to and including n. They take turns choosing prime numbers and removing those numbers and their multiples from the set. The player who cannot make a move loses the game.

Given the number of rounds (x) and an array of values of n for each round (nums), determine the name of the player who won the most rounds. If the winner cannot be determined, return None.

## Function Prototype

```python
def isWinner(x, nums):
    # Your code here
```

### Input
- `x`: The number of rounds (1 <= x <= 10000).
- `nums`: A list of integers representing n for each round (1 <= n <= 10000).

### Output
- The name of the player who won the most rounds: "Maria" or "Ben."
- If the winner cannot be determined, return None.

## Example

Suppose we have the following input:

```python
x = 3
nums = [4, 5, 1]
```

- First round (n=4):
  - Maria picks 2 and removes 2, 4, leaving 1, 3.
  - Ben picks 3 and removes 3, leaving 1.
  - Ben wins because there are no prime numbers left for Maria to choose.

- Second round (n=5):
  - Maria picks 2 and removes 2, 4, leaving 1, 3, 5.
  - Ben picks 3 and removes 3, leaving 1, 5.
  - Maria picks 5 and removes 5, leaving 1.
  - Maria wins because there are no prime numbers left for Ben to choose.

- Third round (n=1):
  - Ben wins because there are no prime numbers for Maria to choose.

In this example, Maria won 1 round, and Ben won 2 rounds. So, the function should return "Ben" as the winner.

## Implementation

To implement this game and determine the winner, you can use a Python function like the following:

```python
def isWinner(x, nums):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1 or (n % 2 == 0 and n != 2):
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
```

This function counts the number of rounds won by Maria and Ben based on whether n is prime or not, and then determines the overall winner based on the count.

## How to Run

You can run this function with your input values like this:

```python
x = 3
nums = [4, 5, 1]
winner = isWinner(x, nums)
print(f"The winner is {winner}")
```

Replace `x` and `nums` with your own input values.

