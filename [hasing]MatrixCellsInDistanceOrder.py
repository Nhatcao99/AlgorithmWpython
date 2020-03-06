def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
    dic, arr = {}, []
    for r in range(R):
        for c in range(C):
            tmp = abs(r - r0) + abs(c - c0)
            if tmp not in dic:
                dic[tmp] = []
            dic[tmp].append([r, c])
    # print(dic)
    for key in sorted(dic):
        arr.extend(dic[key])
    return arr