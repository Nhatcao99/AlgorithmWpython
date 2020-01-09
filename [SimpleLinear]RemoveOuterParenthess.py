def removeOuterParentheses(self, S: str) -> str:
    #PROBLEM:https://leetcode.com/problems/remove-outermost-parentheses
    stack_rank = 0
    string = ""
    for c in S:
        if (c == '('):
            stack_rank += 1
            if (stack_rank > 1):
                string += '('
        if (c == ')'):
            if (stack_rank > 1):
                string += ')'
            stack_rank -= 1
    return string
