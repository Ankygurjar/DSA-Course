







def isSubSquence(s1, s2):

    i = 0
    j = 0
    while i < len(s2) and j < len(s1):
        if s2[i] == s1[j]:
            i += 1
            j += 1
        else:
            j += 1

    return i == len(s2)
















