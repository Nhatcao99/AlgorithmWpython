def subsets(self, nums: List[int]) -> List[List[int]]:
    ls, leng = [], len(nums)

    def subsets(origin_set: List[int], subset: List[int], index: int, n: int):
        if index >= n:
            new_set = []
            new_set.extend(subset)
            ls.append(new_set)
        else:
            new_set = []
            new_set.extend(subset)
            subsets(origin_set, new_set, index + 1, n)
            # print(subset)
            new_set.append(origin_set[index])
            # print(subset)
            subsets(origin_set, new_set, index + 1, n)

    subsets(nums, [], 0, leng)
    return ls
