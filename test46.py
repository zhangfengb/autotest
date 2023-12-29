"""跳格子"""

k = int(input())
arr = []
while True:
    a = input()
    if a:
        arr.append(list(map(int,a.split())))
    else:
        break

def getResult():
    d = {}
    res = []
    for i,j in arr:
        if d.get(i) is None:
            d[i] = []
        d[i].append(j)
        res.append(j)
    kai = []
    for i in range(len(res)):
        if i not in res:
            kai.append(i)


    if len(kai) == 0:
        return 'No'
    tiaoguo = []
    tiaoguo.append(kai[:])
    for k in kai:
        if d.get(k):
            for qi in d[k]:
                tiaoguo.append(qi)

    for i in range(k):
        if i not in tiaoguo:
            return 'No'

    return 'yes'

print(getResult())