def stoneGame(self, piles: List[int]) -> bool:
    sumation = 0
    leng = len(piles)
    while (leng > 0):
        if (leng % 2 != 0):
            tmp = max(piles[0], piles[leng - 1])
            if (tmp == piles[leng - 1]):
                piles.pop()
            else:
                piles.pop(0)
            sumation += tmp
        else:
            tmp = min(piles[0], piles[leng - 1])
            if (tmp == piles[leng - 1]):
                piles.pop()
            else:
                piles.pop(0)
        leng -= 1
    return sumation