arr = list(map(int,input().split()))
n = int(input())
"""滑动窗口"""
def getResult():

    senum = [0,0,0]
    for i in range(n):
        senum[arr[i]] += 1

    maxg = max(senum)

    for i in range(n,len(arr)):
        senum[arr[i]] += 1
        senum[arr[i-n]] -= 1
        maxg = max(maxg,max(senum))

    return maxg

print(getResult())

