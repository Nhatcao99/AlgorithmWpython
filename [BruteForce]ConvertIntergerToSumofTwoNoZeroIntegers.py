def containZero(n: int) -> bool:
    if(n >= 1 and n <= 9):
        return True
    while(n != 0):
        if(n % 10 == 0):
            return False
        n = int(n/10)
    return True

    def getNoZeroIntegers(self, n: int) -> List[int]:
        i = 1
        j = n - 1
        while (i <= j):
            if (containZero(j) and containZero(i)):
                return [i, j]
            i += 1
            j -= 1
