def power(a,n):
    if(a == 0 or n == 0):
        return 0
    if(n % 2 == 0):
        return power(a*a , n/2)
    else:
        return a*power(a*a , n/2)