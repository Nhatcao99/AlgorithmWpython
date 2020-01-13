def repeatedNTimes(self, A: List[int]) -> int:
    total_hash = {}
    leng = len(A)
    for i in range(0, leng):
        if (A[i] not in total_hash):
            total_hash[A[i]] = 1
        else:
            return A[i]