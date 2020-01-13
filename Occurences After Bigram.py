def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
    wordList = re.sub("[^\w]", " ", text).split()
    print(wordList)
    result = []
    leng = len(wordList)
    for i in range(0, leng - 2):
        if (wordList[i] == first and wordList[i + 1] == second):
            result.append(wordList[i + 2])
    return result
