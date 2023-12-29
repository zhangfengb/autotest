"""
c,k = list(map(int,input().split()))
n = int(input())
qiang = [list(map(int,input().split())) for _ in range(n)]


def dfs(mg,i,j):
    if i >= c or j >= k:
        return False
    if mg[i][j] == 1:
        return True
    if mg[i][j] == 2:
        return False
    if mg[i][j] == -1:
        return False

    if mg[i][j] == 0:
        # 向下
        xia = dfs(mg,i+1,j)
        # 向上
        shang = dfs(mg,i,j+1)
        if xia or shang:
            mg[i][j] = 1
        else:
            mg[i][j] = -1

    return mg[i][j] == 1




def garResult():
    mg = [[0 for _ in range(k)] for _ in range(c)]
    for i,j in qiang:
        mg[i][j] = 2

    mg[c-1][k-1] = 1
    print(mg)
    dfs(mg,0,0)
    print(mg)

garResult()
"""
import re

s = input()

def getResult():
    res = []
    stack = []
    for c in s:
        if c == '0':
            if len(stack) != 0 and stack[-1] == '0':
                tmp = "".join(stack)
                res.append(tmp)
                stack.clear()
        stack.append(c)

    if stack is not None:
        tmp = "".join(stack)
        res.append(tmp)
        stack.clear()
    res = list(filter(lambda x:x!= '00' and x!='0',res))
    jieguo = []
    for xin in res:
        if re.match(r'^(01)+0$',xin) is not None:
            jieguo.append(xin)
    jieguo.sort(key = lambda x:-len(x))
    print(jieguo[0])
#00101010101100001010010
getResult()
