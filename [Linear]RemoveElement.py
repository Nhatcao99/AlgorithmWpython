def removeElement(self, nums: List[int], val: int) -> int:
    # IDEA:it doesn't matter what is stored so if the element acceptable
    # let it in array
    # else , don't include
    index = 0
    for i in range(0, len(nums)):
        if (nums[i] != val):
            nums[index] = nums[i]
            index += 1  # this will replace every val with sth not val
    return index  # return the array length with no val