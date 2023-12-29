"""内存分配"""

nc = input().split(',')
xqs = list(map(int,input().split(',')))

def getResult():
    ncd = {}
    res = []
    keys = []
    for n in nc:
        dx,num = n.split(':')
        if ncd.get(dx) is None:
            ncd[dx] = int(num)
        keys.append(int(dx))

    keys.sort()

    for xq in xqs:
        for key in keys:
            if key > xq and ncd[str(key)] > 0:
                ncd[str(key)] -= 1
                res.append(xq)
                break
    temp = []
    for xq in xqs:
        if xq in res:
            temp.append('True')
        else:
            temp.append('False')

    print(','.join(temp))

getResult()

"""
64:2,128:1,32:4,1:128
50,36,64,128,127
"""

