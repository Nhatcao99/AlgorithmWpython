def singleNumber(self, nums: List[int]) -> List[int]:
    dic = {}
    ls = []
    for e in nums:
        if e in dic:
            dic[e] += 1
        else:
            dic[e] = 1
    for e in dic:
        if dic[e] == 1:
            ls.append(e)
    return ls