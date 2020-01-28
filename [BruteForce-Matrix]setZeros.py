def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    n = len(matrix[0])
    visit = numpy.zeros((m, n))
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                if visit[i][j] != 1:
                    visit[i][j] = 1
                    for k in range(n):
                        if matrix[i][k] != 0:
                            visit[i][k] = 1
                            matrix[i][k] = 0
                    for k in range(m):
                        if matrix[k][j] != 0:
                            visit[k][j] = 1
                            matrix[k][j] = 0