n = int(input())
s = [input() for _ in range(n)]

def dfs(s):
    a = [1,2,4]
    if n > 3:
        for i in range(3,n):
            tem = a[i-1] + a[i-2] + a[i-3]
            a.append(tem)

    al = list(s)
    for i in range(len(al)):
        al[i] = (a[i]+(ord(al[i])-97)) % 26 +97

    return "".join(map(chr,al))

for i in range(n):
    print(dfs(s[i]))