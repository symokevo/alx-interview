# Island Perimeter Calculator

## Overview

This Python function, `island_perimeter(grid)`, calculates the perimeter of an island described in a grid. The grid consists of cells representing land and water, and the function determines the total perimeter of the island within the grid. The following information describes the grid and how the function works:

- **Grid Structure**: The grid is a list of lists of integers, where:
    - `0` represents water.
    - `1` represents land.
    - Each cell is square with a side length of 1.
    - Cells are connected horizontally and vertically (not diagonally).
    - The grid is rectangular, with both its width and height not exceeding 100.
    - The grid is completely surrounded by water.
    - There is either one island or nothing in the grid.
    - The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island).

## Function Usage

To use the `island_perimeter(grid)` function, follow these steps:

1. **Import the Function**: Import the function into your Python script or interactive environment.

    ```python
    from island_perimeter import island_perimeter
    ```

2. **Create a Grid**: Define a grid as a list of lists, where each inner list represents a row of the grid. Populate the grid with `0` for water and `1` for land.

    ```python
    grid = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]
    ```

3. **Calculate the Perimeter**: Call the `island_perimeter(grid)` function, passing your grid as an argument.

    ```python
    perimeter = island_perimeter(grid)
    ```

4. **Retrieve the Perimeter**: The `perimeter` variable now contains the total perimeter of the island in your grid.

## Example

Here's a simple example of how to use the function:

```python
from island_perimeter import island_perimeter

# Define the grid
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

# Calculate the perimeter
perimeter = island_perimeter(grid)

# Print the result
print("Island Perimeter:", perimeter)
```

In this example, the `perimeter` variable will contain the calculated perimeter of the island in the provided grid.

## Notes

- This function assumes that the input grid adheres to the specified constraints and that there is either one island or nothing in the grid.
- It calculates the perimeter efficiently by iterating through the grid, identifying land cells, and counting shared edges with adjacent land cells.

Feel free to use this `island_perimeter` function in your Python projects to calculate the perimeter of islands within grids!