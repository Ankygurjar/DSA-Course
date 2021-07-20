






from collections import Counter


def anaGram(s1, s2):

    countS1 = Counter(s1)
    countS2 = Counter(s2)
    if len(s2) > len(s1):
        for i in s2:
            if i not in s1:
                return False
            elif countS2.get(i) != countS1.get(i):
                return False
        return True
    else:
        for i in s1:
            if i not in s2:
                return False
            elif countS2.get(i) != countS1.get(i):
                return False
        return True

















