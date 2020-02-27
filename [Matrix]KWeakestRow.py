def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    dic, ls, count = {}, [], 0
    m, n = len(mat), len(mat[0])
    for i in range(m):
        soldier = 0
        for j in range(n):
            if mat[i][j] == 1: soldier += 1
        if soldier not in dic:
            dic[soldier] = []
        dic[soldier].append(i)
    for key in sorted(dic.keys()):
        if count == k: break
        leng, i = len(dic[key]) - 1, 0
        while (i <= leng and count < k):
            ls.append(dic[key][i])
            count += 1
            i += 1
    return ls