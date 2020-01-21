def sortArrayByParity(self, A: List[int]) -> List[int]:
    # applying insertion sort will actually making thing faster but I am lazy
    arr = []
    index = 0
    for c in A:
        if c % 2 != 0:
            arr.append(c)
        else:
            arr.insert(index, c)
            index += 1
    return arr