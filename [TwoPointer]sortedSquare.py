def sortedSquares(self, A: List[int]) -> List[int]:
    ls = []
    index_pos, index_neg = 0, 0
    leng = len(A)
    for i in range(leng):
        if A[i] >= 0:
            index_pos = i
            break
    index_neg = index_pos - 1
    while index_pos <= leng - 1 and index_neg >= 0:
        tmp1, tmp2 = A[index_pos] * A[index_pos], A[index_neg] * A[index_neg]
        # print(index_pos , index_neg)
        if tmp1 < tmp2:
            ls.append(tmp1)
            index_pos += 1
        if tmp1 == tmp2:
            ls.append(tmp1)
            ls.append(tmp2)
            index_pos += 1
            index_neg -= 1
        if tmp1 > tmp2:
            ls.append(tmp2)
            index_neg -= 1

    while index_pos <= leng - 1:
        ls.append(A[index_pos] * A[index_pos])
        index_pos += 1
    while index_neg >= 0:
        ls.append(A[index_neg] * A[index_neg])
        index_neg -= 1
    return ls