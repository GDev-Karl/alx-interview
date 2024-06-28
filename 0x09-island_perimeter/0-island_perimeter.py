#!/usr/bin/python3
"""Define a function that returns the perimeter of an island in grid."""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""

    if not grid or not grid[0]:
        return 0

    height = len(grid) - 2
    width = len(grid[0]) - 2

    return height * width