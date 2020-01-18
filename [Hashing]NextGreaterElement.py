def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # iterate from the end of nums2 , if a[i] element smaller than the a[i+1] element, a[i+1] is the greater ele , else a[i + 1] 's greater ele is the greater ele of a[i]
    greater = {}
    leng1 = len(nums1)
    leng2 = len(nums2)
    if (leng1 == 0):
        return []
    if (leng2 == 0):
        return [-1] * leng1
    greater[nums2[leng2 - 1]] = -1
    index = leng2 - 2
    while (index >= 0):
        if (nums2[index] < nums2[index + 1]):
            greater[nums2[index]] = nums2[index + 1]
        else:
            if (nums2[index] > greater[nums2[index + 1]]):
                tmp = greater[nums2[index + 1]]
                while (tmp < nums2[index]):
                    if tmp == -1:
                        greater[nums2[index]] = -1
                        break
                    tmp = greater[tmp]
                    if (tmp > nums2[index]):
                        greater[nums2[index]] = tmp
                        break
            else:
                greater[nums2[index]] = greater[nums2[index + 1]]
        index -= 1
    for i in range(0, leng1):
        nums1[i] = greater[nums1[i]]
    return nums1
