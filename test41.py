s = input()
m = int(input())
tags = []
for i in range(m):
    tag = int(input())
    tags.append(tag)




def dfs():
    res = {}
    for i in range(len(s)-3):
        ntag = int(s[i:i+2],16)
        nlen = int(s[i+2:i+4],16)
        xinxi = s[i+4:i+4+nlen*2]
        offset = (i+5)//2
        i = i + 3 + nlen*2

        if i >= len(s):
            break

        res[ntag] = [nlen,offset]
    for tag in tags:
        if res.get(tag) is not None:
            print(' '.join(map(str,res[tag])))
        else:
            print('0 0')
