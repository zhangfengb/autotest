n,m = map(int,input().split())
word = input()
jz = [list(input()) for _ in range(n)]
"""矩阵中找单词"""
def go(i,j,used,word,jz,ind,res):
    t,k = i,j
    if ind == len(word)-1:
        res.append('1')
        return
    if jz[t][j] == word[ind]:
        used[t][j] = True
        if j - 1 >= 0 and not used[t][j-1]:
            go(t, j-1, used, word, jz, ind+1,res)
        if j + 1 < m and not used[t][j+1]:
            go(t, j+1, used, word, jz, ind+1,res)
        if t - 1 >= 0 and not used[t-1][j]:
            go(t-1, j, used, word, jz, ind+1,res)
        if t + 1 < n and not used[t+1][j]:
            go(t+1, j, used, word, jz, ind+1,res)

        used [t][j] = False

def dfs():
    res = []
    for i in range(n):
        for j in range(m):
            go(i,j,[[False]*m for _ in range(n)],word,jz,0,res)
            if res:
                return [i+1,j+1]

alist = dfs()
print(" ".join(map(str,alist)))