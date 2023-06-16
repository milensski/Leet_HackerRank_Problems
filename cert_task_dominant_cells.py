#!/bin/python3

import os


#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def numCells(grid):
    # Write your code here
    neightbours = [
        [0, -1],
        [0, 1],
        [-1, 0],
        [1, 0],
        [-1, -1],
        [-1, 1],
        [1, -1],
        [1, 1]
    ]

    counter = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):

            pawn = grid[row][col]

            for r, c in neightbours:
                if (row + r >= 0 and row + r < len(grid)) and (col + c >= 0 and col + c < len(grid[row])):
                    enemy = grid[row + r][col + c]

                    if pawn <= enemy:
                        break
            else:

                counter += 1

    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
