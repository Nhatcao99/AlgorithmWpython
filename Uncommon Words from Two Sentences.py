def uncommonFromSentences(self, A: str, B: str) -> List[str]:
    hash1 = {}
    hash2 = {}
    A = re.sub("[^\w]", " ", A).split()
    B = re.sub("[^\w]", " ", B).split()
    leng1, leng2 = len(A), len(B)
    for i in range(0, leng1):
        if (A[i] not in hash1):
            hash1[A[i]] = 1
        else:
            hash1[A[i]] += 1
    for i in range(0, leng2):
        if (B[i] not in hash2):
            hash2[B[i]] = 1
        else:
            hash2[B[i]] += 1
    result = []
    for key, value in hash1.items():
        if (value == 1 and key not in hash2):
            result.append(key)
    for key, value in hash2.items():
        if (value == 1 and key not in hash1):
            result.append(key)
    return result