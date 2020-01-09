def plusOne(self, digits: List[int]) -> List[int]:
    #Problem: https://leetcode.com/problems/plus-one
    index = len(digits) - 1
    if (digits[index] < 9):
        digits[index] += 1
    else:
        remember = 1;
        while (remember == 1 and index > 0):
            digits[index] = 0
            index -= 1
            if (digits[index] != 9):
                digits[index] += 1
                remember = 0
        if (remember == 1):
            digits[0] = 0
            digits.insert(0, 1)
    return digits