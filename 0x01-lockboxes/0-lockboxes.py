#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially
from 0 to n - 1 and each box may
contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    :param boxes: List of lists, where each sublist contains keys to other boxes.
    :return: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    opened = [False] * n  # Track if each box is opened
    opened[0] = True  # Box 0 is always open
    keys = [0]  # Start with the key to the first box

    while keys:
        current = keys.pop(0)  # Take the next key
        for key in boxes[current]:
            if key < n and not opened[key]:  # Check if the key opens a valid and unopened box
                opened[key] = True
                keys.append(key)

    # Check if all boxes are opened
    return all(opened)
