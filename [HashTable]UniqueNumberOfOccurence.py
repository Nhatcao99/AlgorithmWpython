def uniqueOccurrences(self, arr: List[int]) -> bool:
    hash1 = {}  # store number of apperence
    leng = len(arr)
    for i in range(0, leng):
        if (arr[i] not in hash1):
            hash1[arr[i]] = 1
        else:
            hash1[arr[i]] += 1
    hash2 = {}
    # number of apperence as key and value is the number of "number of apperence"
    # if val > 1 return False
    for key, value in hash1.items():
        if (value not in hash2):
            hash2[value] = 1
        else:
            return False
    return True