






# Not Efficient
def patternSearching(s: str, p: str):
    idxArr = []

    for i in range(len(s)):
        str = ""
        str += s[i]
        for j in range(i + 1, len(s)):
            str += s[j]
            if len(str) == len(p) and str == p:
                idxArr.append(i)
                break

    return idxArr














