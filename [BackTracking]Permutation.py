def permute(self, nums: List[int]) -> List[List[int]]:
    def permutation(num: List[int], s: int, f: int):
        if (s == f):
            ListOfList.append(num[:])
            # to fix the duplicated list
            # when append new element into List in fucntion like this
            # all element might become the same as new element
            # to fix: append(num[:]) in stead of append(num)
        for i in range(s, f + 1):
            num[s], num[i] = num[i], num[s]
            permutation(num, s + 1, f)  # do same thing to other element
            # back track to original so it can work on other case
            num[s], num[i] = num[i], num[s]

    ListOfList = []
    permutation(nums, 0, len(nums) - 1)
    return ListOfList