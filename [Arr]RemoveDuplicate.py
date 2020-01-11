def removeDuplicates(self, nums: List[int]) -> int:
    count = 0  # variance of the new size increment by 1 for each swap action
    leng = len(nums)
    i = 0  # i standard to compare
    j = 1  # used to track value diffent from i
    while (i < leng - 1 and j <= leng - 1):
        if (nums[i] == nums[leng - 1]):
            # 1 variable
            # j hit end
            # array have one ele only
            break
        if (nums[i] == nums[j]):
            j += 1
        if (nums[i] != nums[j]):
            nums[i + 1], nums[j] = nums[j], nums[i + 1]
            i += 1
            j += 1
            count += 1
    return count + 1
