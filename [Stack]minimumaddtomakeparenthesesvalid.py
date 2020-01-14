def minAddToMakeValid(self, S: str) -> int:
    num_stack1 = 0
    num_stack2 = 0
    for c in S:
        if c == '(':
            num_stack1 += 1
        if c == ')':
            if num_stack1 > 0:
                num_stack1 -= 1
            else:
                num_stack2 += 1
    return num_stack1 + num_stack2