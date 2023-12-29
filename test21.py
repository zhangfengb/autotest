k = int(input())

def dfs(k):
    if k <= 4:
        return k
    i = 4
    res = 0
    while i <= k:
        if '4' in str(i):
            res += 1
        i += 1

    return k - res

print(dfs(k))
