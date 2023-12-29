"""扩散"""
import math

arr = list(map(int,input().split(',')))

def getResult():
    n = int(math.sqrt(len(arr)))

    jz = [[0 for _ in range(n)] for _ in range(n)]
    wuran = []
    total = len(arr) #未污染地方
    for i in range(n):
        for j in range(n):
            if arr[i*n + j] == 1:
                jz[i][j] = 1
                wuran.append([i,j])
                total -= 1

    if len(wuran) == 0 or total == len(arr):
        return '-1'

    while len(wuran) >0 and total > 0:
        wri,wrj = wuran.pop(0)
        offset = ((0,1),(0,-1),(1,0),(-1,0))
        for fx,fy in offset:
            newI = wri + fx
            newJ = wrj + fy

            if 0 <= newI < n and 0 <= newJ < n and jz[newI][newJ] == 0:
                tian = jz[wri][wrj] + 1
                jz[newI][newJ] = tian
                wuran.append([newI,newJ])
                total -= 1

                if total == 0:
                    return tian-1

print(getResult())

