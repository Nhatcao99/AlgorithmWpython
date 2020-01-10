def majorityElement(self, nums: List[int]) -> int:
    dictionary = {}
    for i in range(0, len(nums)):
        if (nums[i] in dictionary):
            dictionary[nums[i]] += 1
        else:
            dictionary[nums[i]] = 1
    major = nums[0]
    for key, value in dictionary.items():
        if (dictionary[key] > dictionary[major]):
            major = key
    return major