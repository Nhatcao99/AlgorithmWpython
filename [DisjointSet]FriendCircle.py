def findCircleNum(self, M: List[List[int]]) -> int:
    n = len(M)
    # print(n)
    arr, size, visited = [0] * n, [1] * n, [0] * n
    for i in range(n):
        arr[i] = i
    for i in range(n):
        for j in range(n):
            if M[i][j] == 1:
                # print(i,j)
                tmp1, tmp2 = i, j
                while (tmp1 != arr[tmp1]): tmp1 = arr[tmp1]
                while (tmp2 != arr[tmp2]): tmp2 = arr[tmp2]
                if tmp1 != tmp2:
                    if size[tmp1] >= size[tmp2]:
                        size[arr[i]] += size[arr[j]]
                        arr[arr[j]] = arr[i]
                        # print(arr, size)
                    else:
                        size[arr[j]] += size[arr[i]]
                        arr[arr[i]] = arr[j]
                        # print(arr, size)
    # print(arr,size)
    count_group = 0
    for i in range(n):
        if visited[i] == 0:
            tmp = arr[i]
            while (tmp != arr[tmp]): tmp = arr[tmp]
            if visited[tmp] == 0:
                visited[i] = 1
                visited[tmp] = 1
                count_group += 1
    return count_group