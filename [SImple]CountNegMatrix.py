def countNegatives(self, grid: List[List[int]]) -> int:
    i, count = len(grid) - 1, 0
    while (i >= 0):
        j = len(grid[i]) - 1
        while (j >= 0 and grid[i][j] < 0):
            count += 1
            j -= 1
        i -= 1
    return count