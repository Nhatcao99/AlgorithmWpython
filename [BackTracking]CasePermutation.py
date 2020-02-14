def letterCasePermutation(self, S: str) -> List[str]:
    ls = []  # list store stirng

    def UpperCaseInCharacter(S: str, index: int) -> str:
        s = list(S)
        s[index] = s[index].upper()
        return "".join(s)

    def LowerCaseInCharacter(S: str, index: int) -> str:
        s = list(S)
        s[index] = s[index].lower()
        return "".join(s)

    def CasePer(S: str, index: int, n: int):
        if index >= n:
            ls.append(S)
        else:
            CasePer(S, index + 1, n)
            if S[index].isalpha():
                if S[index].islower():
                    S = UpperCaseInCharacter(S, index)
                    CasePer(S, index + 1, n)
                else:
                    S = LowerCaseInCharacter(S, index)
                    CasePer(S, index + 1, n)

    CasePer(S, 0, len(S))
    return ls