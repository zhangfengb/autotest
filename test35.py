alist = list(map(int,input().split()))
c = alist[0]
b = alist[1]
arr = alist[2:]

def helps(num):

    st = hex(num)[2:]
    if len(st)%2 == 1:
        st = '0' + st

    sumA = 0
    for i in range(0,len(st),2):
        sumA += int(st[i:i+2],16)

    res = sumA % b
    return res

def dfs():
    temp = {}
    for i in range(len(arr)):
        res = helps(arr[i])
        if res < c:
            if temp.get(res) is None:
                temp[res] = 0
            temp[res] += 1

    return max(temp.values())
# 3 4 256 257 258 259 260 261 262 263 264 265
print(dfs())