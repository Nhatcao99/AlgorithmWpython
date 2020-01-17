def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
    absolute = {}  # store all possibble absolute and their tuple
    leng = len(arr)
    arr.sort()
    minimum = arr[2] - arr[1]
    for i in range(0, leng - 1):
        tmp = arr[i + 1] - arr[i]
        if tmp < minimum:
            minimum = tmp  # save the smallest absote
        if tmp not in absolute:
            # create a list of list that conect to the abs
            absolute[tmp] = []
        absolute[tmp].append([arr[i], arr[i + 1]])  # adding to an existing key
    # for c in absolute:
    #     absolute[c].sort(key=lambda x: x[0])
    return absolute[minimum]
