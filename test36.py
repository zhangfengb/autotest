m = int(input())

tasks = [[] for _ in range(m)]

for i in range(m):
    n = int(input())
    task = [[] for _ in range(n)]
    for j in range(n):
        task[j] = list(map(int,input().split()))
    tasks[i] = task


def dfs():
    for task in tasks:

        task.sort(key=lambda x:-x[1])
        nlen = len(task)

        dp = [0] * nlen
        dp[0] = task[0][0] + task[0][1]
        for i in range(1,nlen):
            print(i)
            dp[i] = max(dp[i-1],dp[i-1]-task[i-1][1]+task[i][0]+task[i][1])
        print(dp)
        print(dp[nlen-1])

dfs()
