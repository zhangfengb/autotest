n,k = map(int,input().split())
arr = list(map(int,input().split()))

def dfs():

    sumL = [0]*(n+1)

    for i in range(1,n):
        sumL[i] = sumL[i-1] + arr[i]

    l = 0
    r = 1
    ans = 0
    while r <= n:
        if sumL[r] - sumL[l] >= k:
            ans += n - r + 1
            l += 1
            r = l+1
        else:
            r += 1

    return ans

print(dfs())
