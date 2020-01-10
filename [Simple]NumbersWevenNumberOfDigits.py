def findNumbers(self, nums: List[int]) -> int:
    count = 0
    for i in range(0, len(nums)):
        digit_amount = len(str(nums[i]))
        if (digit_amount % 2 == 0):
            count += 1
    return count