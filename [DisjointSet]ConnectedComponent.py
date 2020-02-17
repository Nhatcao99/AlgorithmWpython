def componentsInGraph(n):
    #
    # Write your code here.
    #
    n = len(gb)
    arr , size , visited = [],[],[]
    m = n * 2
    for i in range(m):
        arr.append(i)
        visited.append(0)
        size.append(1)
    for c in range(n):
        x,y = gb[c][0] , gb[c][1]
        x -= 1
        y -= 1
        if size[arr[x]] >= size[arr[y]]:
            size[arr[x]] += size[arr[y]]
            arr[arr[y]] = arr[x]
        else:
            size[arr[y]] += size[arr[x]]
            arr[arr[x]] = arr[y]
    # print(size , arr)
    maximus , minimus = 1 , 15000
    for i in range(m):
        if visited[i] == 0:
            tmp = i
            while(tmp != arr[tmp]):
                tmp = arr[tmp]
            if maximus < size[tmp] and size[tmp] > 1:
                maximus = size[tmp]
            if minimus > size[tmp] and size[tmp] > 1:
                minimus = size[tmp]
            visited[tmp] = 1
            visited[i] = 1
            # print(visited , size)
    print(minimus,maximus)