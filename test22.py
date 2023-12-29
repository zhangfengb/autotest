n = int(input())

def dfs(n):
    res = []
    tem = []
    for i in range(n):
        tem.append(i+1)
    k = 1
    m = 0
    total = tem[0]
    while m < n:
        if total > n:
            total -= tem[m]
            m += 1
        elif total == n:
            res.append(tem[m:k])
            total -= tem[m]
            m += 1
            if k < n:
                total += tem[k]
                k += 1

        else:

            total += tem[k]
            k += 1
    res.sort(reverse=True)
    for alist in res:
        str1 = "+".join(map(str,alist))
        print(str(n) + '=' + str1)
    print("Result:"+str(len(res)))

dfs(n)