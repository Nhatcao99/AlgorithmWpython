#problem description: a grid m x n with a robot on top
#robot can only move down and right
#find paths robot reach the bottom end
def uniquePaths(self, m: int, n: int) -> int:
    # approach dynamic programing , bottom up with a top down grid
    # will be pretty fast but cost memory
    path_memoi = [[1 for j in range(n)] for i in range(m)]
    # make an memoi grid to store number of step , for every square on the edge ,
    # init as 1
    for i in range(1, m):
        for j in range(1, n):
            path_memoi[i][j] = path_memoi[i - 1][j] + path_memoi[i][j - 1]
    return path_memoi[m - 1][n - 1]
