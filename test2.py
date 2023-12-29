s=input()

def helpdfs(num):
    tem = hex(num)[2:]
    if len(tem)==1:
        tem = '0'+tem
    return tem

def dfs(s):
    stack = s.split("#")


    if len(stack) != 4:
        return "invalid"

    try:
        p1,p2,p3,p4 = map(int,stack)

        if 128>=p1>=0 and 256>=p2>=0 and 256>=p3>=0 and 256>=p4>=0:
            temp = helpdfs(p1) +helpdfs(p2) +helpdfs(p3) +helpdfs(p4)
            print(type(temp))
            return int(temp,16)
        else:
            return "invalid"
    except:
        return "invalid"

print(dfs(s))