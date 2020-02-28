def commonChars(self, A: List[str]) -> List[str]:
    leng, list_dic, answer = len(A), [], []
    for i in range(leng):
        dic = {}
        for c in A[i]:
            if c not in dic:
                dic[c] = 0
            dic[c] += 1
        list_dic.append(dic)
    # print(list_dic)
    for key in list_dic[0]:
        minimum = list_dic[0][key]
        # print(minimum)
        for i in range(1, leng):
            if key not in A[i]:
                minimum = 0
                break
            else:
                minimum = min(minimum, list_dic[i][key])
        for j in range(minimum):
            answer.append(key)
    return answer
