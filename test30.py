"""喊7"""
arr = list(map(int,input().split()))

def dfs():
    total = 0
    for i in arr:
        total += i

    res = [0] * len(arr)
    j = 1
    t = 0
    while total > 0:
        if j % 7 == 0 or '7' in str(j):
            res[t%len(arr)] += 1
            total -= 1
        j += 1
        t += 1

    return ' '.join(map(str,res))

print(dfs())
