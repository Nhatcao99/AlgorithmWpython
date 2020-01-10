def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    dictionary = {}
    for i in range(0, len(nums)):
        if (nums[i] in dictionary):
            start = dictionary.get(nums[i])
            dist = i - start
            if (dist <= k):
                return True
            else:
                dictionary[nums[i]] = i
        else:
            dictionary[nums[i]] = i
    return False