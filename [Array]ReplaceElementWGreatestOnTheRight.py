def replaceElements(self, arr: List[int]) -> List[int]:
    current_greatest = -1
    index = len(arr) - 1
    ls = []
    while (index >= 0):
        ls.insert(0, current_greatest)
        if (arr[index] > current_greatest):
            current_greatest = arr[index]
        index -= 1
    return ls