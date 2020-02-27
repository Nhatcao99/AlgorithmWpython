def search(self, nums: List[int], target: int) -> int:
    def BinSearch(nums: List[int], start: int, end: int, target: int):
        result = -1
        if start == end:
            if nums[start] == target:
                return start
            else:
                return -1
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return BinSearch(nums, start, mid, target)
        else:
            return BinSearch(nums, mid + 1, end, target)

    n = len(nums)
    return BinSearch(nums, 0, n - 1, target)
#