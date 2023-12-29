names = input().split(',')
sx = input()

def dfs(name,sx,indx,start,res):
    if start == len(sx) and indx >= len(name.split()):
        res.append(name)
        return

    xm = name.split()
    for i in range(indx,len(xm)):
        part = xm[i]
        for j in range(len(part)):
            if start < len(sx) and part[j] == sx[start]:
                start += 1
                dfs(name,sx,indx+1,start,res)



def getResult():
    res = []

    for name in names:
        dfs(name,sx,0,0,res)

    if res:
        return ','.join(res)
    else:
        return 'no find'

print(getResult())