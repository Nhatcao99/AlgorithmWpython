def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # use can't use list as hashable so let use string representationof the list instead
    dictionary, ls = {}, []  # key: list's string representation , value: the list of string
    for s in strs:
        arr = [0] * 26
        for c in s:
            arr[ord(c) - 97] += 1
        string_rep = repr(arr)
        if string_rep not in dictionary:
            dictionary[string_rep] = []
        dictionary[string_rep].append(s)
    for key, value in dictionary.items():
        ls.append(value)
    return ls