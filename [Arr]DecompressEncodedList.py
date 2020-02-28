def decompressRLElist(self, nums: List[int]) -> List[int]:
    arr, leng = [], len(nums)
    for i in range(0, leng, 2):
        tmp = [nums[i + 1]] * nums[i]
        arr.extend(tmp)
    return arr