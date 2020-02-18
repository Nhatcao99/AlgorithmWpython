def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    n = len(edges)
    arr, size = [0] * n, [1] * n
    for i in range(n):
        arr[i] = i
    for tup in edges:
        x, y = tup[0] - 1, tup[1] - 1
        tmp1, tmp2 = arr[x], arr[y]
        while tmp1 != arr[tmp1]:
            tmp1 = arr[tmp1]
            arr[x] = tmp1
        while tmp2 != arr[tmp2]:
            tmp2 = arr[tmp2]
            arr[y] = tmp2
        if tmp1 != tmp2:
            if size[arr[x]] >= size[arr[y]]:
                size[arr[x]] += size[arr[y]]
                size[arr[y]] = size[arr[x]]
                arr[arr[y]] = arr[x]
                # print(arr,size)
            else:
                size[arr[y]] += size[arr[x]]
                size[arr[x]] = size[arr[y]]
                arr[arr[x]] = arr[y]
                # print(arr,size)
        else:
            return tup
