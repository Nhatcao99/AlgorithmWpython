def canThreePartsEqualSum(self, A: List[int]) -> bool:
    total = 0
    for c in A: total += c
    i, j = 0, len(A) - 1
    sum1, sum2 = 0, 0
    if total % 3 != 0:
        return False
    target = total / 3
    while (i < j):
        if sum1 == target and sum2 == target: return True
        if sum1 != target:
            while sum1 != target and i < j:
                sum1 += A[i]
                if sum1 == target: break
                i += 1

        if sum2 != target:
            while sum2 != target and j > i:
                sum2 += A[j]
                if sum2 == target: break
                j -= 1
    return False