def freqAlphabets(self, s: str) -> str:
    dic, n, st, i = {}, len(s), "", 0
    for c in range(26):
        if c < 9:
            dic[str(c + 1)] = chr(c + 97)
        else:
            tmp = str(c + 1) + '#'
            dic[tmp] = chr(c + 97)
    # print(dic)
    while i < n:
        if i < n - 2:
            if s[i + 2] == '#':
                tmp = s[i] + s[i + 1] + s[i + 2]
                st += dic[tmp]
                i += 2
            else:
                st += dic[s[i]]
        else:
            st += dic[s[i]]
        i += 1
    return st
