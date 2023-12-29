k = int(input())
s = input()

def convert(s):
    lowcount = 0
    uppercount = 0

    for c in s:
        if 'a'<=c <='z':
            lowcount += 1
        if 'A'<=c<='Z':
            uppercount += 1

    if lowcount > uppercount:
        return s.lower()
    elif lowcount < uppercount:
        return s.upper()
    else:
        return s

def dfs(s,k):
    list1 = s.split('-')
    res= []
    res.append(list1[0])
    str1 = "".join(list1[1:])
    for i in range(0,len(str1),k):
        substr = str1[i:i+k]
        res.append(convert(substr))

    return "-".join(res)

print(dfs(s,k))

