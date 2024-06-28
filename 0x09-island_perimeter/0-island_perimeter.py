#!/usr/bin/python3
"""Define a function that returns the perimeter of an island in grid."""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    height = len(grid) - 2
    width = len(grid[0]) - 2

    return height * width


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
