#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """Returns the perimeter of an island represented
       as a grid matrix with 1s representing lands
       and 0s representing water.
    """
    if not grid or not grid[0]:
        return 0

    land = 1
    perimeter = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] is land:
                perimeter += 4
                if y and grid[y - 1][x] is land:
                    perimeter -= 2
                if x and grid[y][x - 1] is land:
                    perimeter -= 2

    return perimeter