def checkIfExist(self, arr: List[int]) -> bool:
    original, doubled, leng = {}, {}, len(arr)
    for i in range(leng):
        if arr[i] in doubled:
            return True
        if arr[i] * 2 in original:
            return True
        if arr[i] not in original:
            original[arr[i]] = 1
        if arr[i] * 2 not in doubled:
            doubled[arr[i] * 2] = 1
    return False