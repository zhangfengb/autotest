s = input()

def getResult():
    stack = []
    res = []
    biaodian = []
    for i in range(len(s)):
        c = s[i]

        if stack and c == ' ':
            stack.reverse()

            res.append(''.join(stack))
            stack.clear()
            continue
        elif c == '.' or c =='?':
            biaodian.append([i,c])
            continue

        stack.append(c)
    if stack:
        stack.reverse()
        res.append(''.join(stack))
    print(res)
    print(biaodian)
    jieguo = " ".join(res)
    for j,biao in biaodian:
        jieguo = jieguo[:j] + biao +jieguo[j:]
    print(jieguo)



getResult()