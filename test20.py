arr = list(map(int,input().split(',')))
n = int(input())
k = int(input())
"""yue"""
def dfs(arr,n,k):
    res = []
    i = 1
    while len(arr)>0:
        mb = arr.pop(0)
        if i == k:
            res.append(mb)
            k = mb
            i = 1
        else:
            arr.append(mb)
            i += 1

    return ','.join(map(str,res))

print(dfs(arr,n,k))