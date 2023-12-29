"""增强字符串
"""

s = input()
tag = input()

"""def dfs(indx,start,temp,res,lentag):
    if start == len(tag)-1:
        res.append(''.join(temp))
        return

    for i in range(indx,len(s)):
        cc = s[i]
        tack = []
        if tag[start] == '[':

            start += 1
            while tag[start] !=']':

                tack.append(tag[start])
                start += 1


        else:
            tack.append(tag[start])
        print(cc+str(tack))
        if cc in tack:
            print(cc)
            print(tack)
            temp.append(cc)
            dfs(indx+1,start+1,temp,res,lentag)
            temp.pop()
        else:
            return


def getResult():

    res = []
    lentag = 0
    stack = []
    for c in tag:
        if c == '[':
            stack.append(c)
        elif c == ']':

            stack.append(c)
            lentag += 1
            stack.clear()

        elif not stack:
            lentag += 1


    indx = 0
    for i in range(len(s)):
        if s[i] == tag[0]:
            indx = i
            break
    dfs(indx,0,[],res,lentag)
    print(res)"""

def getResult():
    kuai = 0
    man = 0
    start = 0
    while kuai < len(s):
        tack = []

        if tag[start] == '[':
            start += 1
            while tag[start] != ']':
                tack.append(tag[start])
                start += 1
                print(tack)
        else:
            tack.append(tag[start])

        if s[kuai] in tack:
            if start == len(tag)-1:
                return man
            kuai += 1
            start += 1
        else:
            man+=1
            kuai = man
            start = 0

    return -1

print(getResult())