s = input()

def dfs():
    tem = {}
    for i in range(len(s)):
        if tem.get(s[i]) is None:
            tem[s[i]] = 0
        tem[s[i]] += 1
    one = []
    res = []
    for zm,gs in tem.items():
        if gs == 1:
            one.append(zm)
        else:
            if gs%2 == 1:
                gs -=1
                one.append(zm)
            if res:
                for i in range(gs):
                    res.insert(len(res)//2,zm)
            else:
                for i in range(gs):
                    res.append(zm)
    if one:

        res.insert(len(res)//2,one[0])

    return ''.join(res)

print(dfs())
