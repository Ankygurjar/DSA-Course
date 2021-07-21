






# Less Efficient
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

# Better Naive Approach
def search(self,p,s):
        #code here
        
        n = len(s)
        m = len(p)
        for i in range(0, n-m+1):
            j = 0
            while j < m:
                if p[j] != s[i+j]:
                    break
                j += 1
            if j == m:
                return True
        return False












