def NumToNum(n: int) -> int:
    sumation = 0
    while(n != 0):
        sumation += (n%10)*(n%10)
        n = int(n/10)
    return sumation

    def isHappy(self, n: int) -> bool:
        dic = {}  # to store answer , upon loop without 1 break
        dic[n] = 1
        while (n != 1):
            n = NumToNum(n)
            print(n)
            if n not in dic:
                dic[n] = 1
            else:
                return False
        return True


