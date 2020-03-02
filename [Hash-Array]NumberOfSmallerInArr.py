def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    dic, ls = {}, []  # key : the number , value : [number of ocurrence , numbers of smaller in array]
    for c in nums:
        if c not in dic:
            dic[c] = [0, 0]
        dic[c][0] += 1
    # print(dic)
    number_of_smaller = 0
    for key, value in sorted(dic.items()):
        value[1] = number_of_smaller
        number_of_smaller = value[0] + value[1]
    for c in nums:
        ls.append(dic[c][1])
    return ls