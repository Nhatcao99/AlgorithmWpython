def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    hash1 = {}
    hash2 = {}
    result = []
    for ele in nums1:
        if (ele not in hash1):
            hash1[ele] = 1
        else:
            hash1[ele] += 1
    for ele in nums2:
        if (ele not in hash2):
            hash2[ele] = 1
        else:
            hash2[ele] += 1
    for key, val in hash1.items():
        if (key in hash2):
            lesser = min(val, hash2[key])
            while (lesser > 0):
                result.append(key)
                lesser -= 1
    return result