"""连续字母长度"""

s = input()
k = int(input())

def dfs(s):
    s += '0'
    sdict = {}

    c = s[0]
    long = 1
    print(s)
    for i in range(1,len(s)):
        if s[i] == c:
            long += 1
        else:
            if c not in sdict.keys():
                sdict[c] = 0
            sdict[c] = max(sdict[c],long)
            long = 1
            c = s[i]

    res = list(sdict.values())
    res.sort(reverse=True)
    if k >= len(res):
        return -1
    else:
        return res[k-1]


print(dfs(s))