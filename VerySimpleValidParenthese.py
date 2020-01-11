def isValid(self, s):
    while "()" in s or "{}" in s or '[]' in s:
        s = s.replace("()", "").replace('{}', "").replace('[]', "")
        # if s empty return true , else dont return
    return s == ''