n = int(input())
jz = [list(map(str,input().split())) for _ in range(n)]
word = input()

"""找单词"""

def dfs(i,j,level,jz,temp,res):

    offser = ((0,1),(0,-1),(1,0),(-1,0))

    temp.append([i,j])
    if level == len(word)-1:
        res.append(temp[:])
        return res
    tem = jz[i][j]
    jz[i][j] = ''
    for fx,fy in offser:
        newI = i + fx
        newJ = j + fy
        if 0<=newI<n and 0 <= newJ < n and jz[newI][newJ] == word[level+1]:
                dfs(newI,newJ,level+1,jz,temp,res)
    temp.pop()
    jz[i][j] = tem

def getResult():
    res = []
    for i in range(n):
        for j in range(n):
            if jz[i][j] == word[0]:
                dfs(i,j,0,jz,[],res)

    print(res)
getResult()