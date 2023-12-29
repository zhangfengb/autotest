arr = list(map(int,input().split()))
k = int(input())
"""长度大于k的子集"""
def dfs(start,arr,k,temp,res):
    if len(temp) >= k:
        res.append(temp[:])

    for i in range(start,len(arr)):

        dfs(i+1,arr,k,temp+[arr[i]],res)


def getResult():
    res = []
    arr.sort()

    dfs(0,arr,k,[],res)

    for i in range(len(res)):
        print(",".join(map(str,res[i])))

getResult()