s = input()

def dfs(s):

    slist =list(s)
    slist.sort()
    print(slist)
    if s == "".join(slist):
        return s

    res = list(s)
    print(res)
    for i in range(len(res)):
        if slist[i] != res[i]:
            temp = res[i]
            ind = slist.index(temp)
            res[i] = slist[i]
            res[ind] = temp

            break

    return ''.join(res)

print(dfs(s))