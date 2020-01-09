def climbStairs(self, n: int) -> int:
    #PROBLEM: https://leetcode.com/problems/climbing-stairs
    #Mentality: arr[n] = arr[n-1] + arr[n-2]
    arr = [0 for i in range(0, n + 1)]
    if (n < 1):
        return 0
    for i in range(0, n + 1):
        if (i == 0):
            arr[i] = 0
        elif (i == 1):
            arr[i] = 1
        elif (i == 2):
            arr[i] = 2
        else:
            arr[i] = arr[i - 1] + arr[i - 2]
    return arr[n]