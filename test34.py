import math

arr = list(map(int,input().split(',')))
"""污水污染"""
def dfs():
    total = len(arr)
    n = int(math.sqrt(total))
    wsList = []
    tempList = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tempList[i][j] = arr[i*n+j]
            if tempList[i][j] == 1:
                wsList.append([i,j])
                total -= 1
    print(tempList)
    print(wsList)
    ksList = ((0,-1),(0,1),(1,0),(-1,0))
    ind = 0
    if total == len(arr):
        print(-1)
        return
    while total > 0 and len(wsList) >0:
        if ind < len(wsList):
            i,j = wsList[ind]
        for one,two in ksList:
            newI = i + one
            newJ = j +two
            if 0<=newI<n and 0<=newJ<n and tempList[newI][newJ] == 0:
                tempList[newI][newJ] = tempList[i][j]+1
                wsList.append([newI,newJ])
                total -= 1
            if total == 0:
                print(tempList[newI][newJ]-1)
                return tempList[newI][newJ]-1
        ind+=1


#1,0,1,0,0,0,1,0,1
dfs()
