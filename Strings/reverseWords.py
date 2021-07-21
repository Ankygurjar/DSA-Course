def reverseWords(s: str):
    stack = []
    str = ""
    size = len(s)
    for i in range(size):
        if s[i] != " ":
            str += s[i]
        if s[i] == " ":
            stack.insert(0, str)
            str = ""
        if i + 1 == size:
            stack.insert(0, str)
            str = ""
    s = ""
    print(stack)
    for i in stack:
        s += i
        s += " "

    return s
