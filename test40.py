"""欢乐周末"""

m,n = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

def dfs(i,j,count,arr):
    if i >= n or j >= m:
        return
    if arr[i][j] == 1:
        return
    if arr[i][j] == 3:
        count[0] += 1
    fx = ((0,1),(0,-1),(1,0),(-1,0))

    for fx1,fx2 in fx:
        newI = i + fx1
        newJ = j + fx2
        if 0<=newI<n and 0<=newJ<m:
            temp =arr[i][j]
            arr[i][j] = 1
            dfs(newI, newJ, count,arr)
            arr[i][j] = temp
    return count
def getResult():
    ren = []

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                ren.append([i,j])
    x1,y1= ren[0][0],ren[0][1]
    count1 = dfs(x1,y1,[0],arr)
    print(count1)
    print(arr)
    x2,y2= ren[1][0],ren[1][1]
    count2 = dfs(x2,y2,[0],arr)
    print(count2)
    print(arr)
    res = min(count1[0],count2[0])
    print(res)
    return res
getResult()