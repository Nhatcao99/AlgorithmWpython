def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    stack = []
    passed = []
    leng = 0
    for c in asteroids:
        if c > 0:
            stack.append(c)
            leng += 1
        if c < 0:
            if leng > 0:
                tmp = stack[leng - 1]
                while (tmp + c <= 0 and leng > 0):
                    stack.pop()
                    leng -= 1
                    if tmp + c == 0:
                        break
                    if leng > 0:
                        tmp = stack[leng - 1]
                    else:
                        passed.append(c)
            else:
                passed.append(c)
    passed.extend(stack)
    return passed