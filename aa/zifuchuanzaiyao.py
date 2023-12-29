import re

s = input()

def dfs():
    res = []
    zfc = ''
    for i in range(len(s)):
        if re.search('[^a-zA-Z]',s[i]):
            continue
        zfc += s[i]
    zfc = zfc.lower()

    kuai = 1
    man = 0
    tj = {}
    while man < len(zfc) and kuai < len(zfc):
        if tj.get(zfc[man]) is None:
            tj[zfc[man]] = []
        if zfc[kuai] == zfc[man]:

            while zfc[kuai] == zfc[man]:

                kuai += 1
                if kuai >= len(zfc)-1:
                    break

            tj[zfc[man]].append(kuai-man)
            man = kuai
            kuai += 1
        else:
            hou = 0
            kuai += 1
            while kuai < len(zfc):
                if zfc[kuai] == zfc[man]:
                    hou += 1
                    kuai += 1
                else:
                    kuai += 1

            tj[zfc[man]].append(hou)
            man += 1
            kuai = man + 1


    for zm,sz in tj.items():
        for k in sz:
            res.append([zm,k])

    res.sort(key= lambda x:(-x[1],x[0]))
    resstr= ''
    print(res)
    for i in range(len(res)):

        resstr += ''.join(map(str,res[i]))
    return resstr





print(dfs())