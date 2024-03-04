# N Queens Problem Solver

The N Queens Problem Solver is a Python program that finds all possible solutions to the N Queens puzzle. The N Queens puzzle is a classic combinatorial problem where N non-attacking queens need to be placed on an N×N chessboard.

## Usage

To use the program, run it from the command line with the following format:

```
python nqueens.py N
```

Where `N` is an integer greater than or equal to 4, representing the size of the chessboard and the number of queens to be placed.

## Example

To find all solutions for the 4 Queens puzzle, you would run:

```
python nqueens.py 4
```

## How It Works

The program uses a backtracking algorithm to explore all possible solutions efficiently. Here's a brief explanation of how it works:

1. The `is_safe` function is used to determine if a queen can be safely placed at a given position on the chessboard. It checks for conflicts in the same row, column, and diagonals.
2. The `solve_nqueens` function implements recursive backtracking to find all valid solutions. It starts by placing a queen in the first column of the first row and then proceeds to place queens in the subsequent columns. At each step, it checks if the current placement is safe. If so, it proceeds to the next column and repeats the process until all queens are placed. If a valid solution is found, it is added to the list of solutions.
3. The program prints each solution on a separate line, using 'Q' to represent queens and '.' for empty cells on the chessboard.

## Error Handling

The program includes error handling for different scenarios:

1. If the user provides the wrong number of arguments, the program displays a usage message and exits with status 1.
2. If N is not a valid integer, the program displays an error message and exits with status 1.
3. If N is smaller than 4, the program displays an error message and exits with status 1.

## Notes

- The program may take some time to execute for larger N values as the N Queens problem is computationally expensive.
- The solutions are not printed in any specific order.
- The program only uses the `sys` module and doesn't rely on any external libraries.

