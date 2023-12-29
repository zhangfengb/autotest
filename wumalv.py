old = input()
new = input()

def reverStr(s):
    res = ''
    for i in range(0,len(s),2):

        num = int(s[i])
        zf = s[i+1]
        duan = ''
        for i in range(num):
            duan += zf
        res += duan
    return res
def getResult():
    n = 0
    one = reverStr(old)
    two = reverStr(new)
    for i in range(len(one)):
        if one[i]!=two[i]:
            n += 1

    return str(n) + '/'+str(len(one))
print(getResult())