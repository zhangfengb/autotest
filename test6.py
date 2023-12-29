n = int(input())
arr2 = [input().split(",") for _ in range(n)]
"""最大矩阵"""
def dfs(n,arr2):
    res = 0
    for i in range(n):
        maxnum = int("".join(arr2[i]),2)
        for j in range(n):
            arr2[i].insert(0,arr2[i].pop())
            tem = int("".join(arr2[i]),2)
            maxnum = max(maxnum,tem)

        res += maxnum
    return res

print(dfs(n,arr2))