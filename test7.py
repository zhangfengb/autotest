k = int(input())
n = int(input())
wordlist = [input() for _ in range(n)]

""" 单词接龙"""
def dfs():
    res = [wordlist[k]]

    wordict = {}
    for word in wordlist:
        c = word[0]
        if c not in wordict.keys():
            wordict[c] = []
        wordict[c].append(word)

    for ke in wordict.keys():
        wordict[ke].sort(key = lambda x:(-len(x),[ord(c) for c in ke]))

    while True:
        flag = res[-1][-1]
        if flag in wordict.keys():
            res.append(wordict[flag][0])
            wordict[flag].pop(0)
        else:
            break

    return "".join(res)

print(dfs())