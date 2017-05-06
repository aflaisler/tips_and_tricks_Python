from memory_profiler import profile
from collections import deque
import numpy as np
import pandas as pd


def ant(grid, col, row, n, dir=0):
    for _ in range(n):
        # turn
        color = grid[row][col]
        if color == 1:
            dir = (dir + 1) % 4
        elif color == 0:
            dir = (dir - 1) % 4

        # flip color
        grid[row][col] ^= 1

        # move forward
        if dir == 0:
            row -= 1
        elif dir == 1:
            col += 1
        elif dir == 2:
            row += 1
        elif dir == 3:
            col -= 1

        # expand grid
        if row < 0:
            grid.insert(0, [0] * len(grid[0]))
            row = 0
        if row == len(grid):
            grid.append([0] * len(grid[0]))
        if col < 0:
            for i in range(len(grid)):
                grid[i].insert(0, 0)
            col = 0
        if col == len(grid[0]):
            for i in range(len(grid)):
                grid[i].append(0)

    return grid


x = ant(grid=[[1]], col=0, row=0, n=13000, dir=0)
