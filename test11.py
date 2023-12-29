fxlist = input().split()
n,m = map(int,input().split())
jz = [input().split() for _ in range(n)]
"""贪吃蛇"""
def go(i, j, fx, snke):
    i1 = i
    j1 = j
    if fx == 'D':
        i1 += 1
    if fx == 'U':
        i1 -= 1
    if fx == 'L':
        j1 -= 1
    if fx == 'R':
        j1 += 1


    if i1 < 0 or i1 >= n or j1 < 0 or j1 >= m:
        return len(snke)
    else:
        if jz[i1][j1] == 'E':
            jz[i1][j1] = 'H'
            snke.insert(0,[i1,j1])
            x,y = snke.pop()
            jz[x][y] = 'E'
        elif jz[i1][j1] == 'F':
            jz[i1][j1] = 'H'
            snke.insert(0, [i1, j1])
        else:
            return len(snke)
    return 0


def dfs():
    snke = []
    for i in range(n):
        for j in range(m):
            if jz[i][j] == 'H':
                snke.append([i,j])

    fx = 'L'

    for fx1 in fxlist:
        if fx1 == 'G':
            print(fx)
            i, j = map(int,snke[0])
            res = go(i,j,fx, snke)
            print(snke)
            if res>0:
                return res
        else:
            fx = fx1

    return len(snke)

print(dfs())