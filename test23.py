import sys

n,m = map(int,input().split())
times = [list(map(int,input().split())) for _ in range(m)]
src,dist = map(int,input().split())

def dfs(n,times,src,dist):

    graph = {}

    for u, v, w in times:
        if u not in graph.keys():
            graph[u] = []
        graph[u].append([v,w])
    print(graph)
    alist = [sys.maxsize for _ in range(n+1)]

    alist[src] = 0

    need = []

    while True:
        flag = False

        if src in graph.keys():

            for v,w in graph[src]:
                newD = alist[src] + w

                if newD >= alist[v]:
                    continue

                alist[v] = newD

                if v not in need:
                    need.append(v)
                    flag = True

        if len(need) == 0:
            break

        if flag:
            need.sort(key = lambda x:alist[x])

        src = need.pop(0)
        print(alist)
    return -1 if alist[dist] == sys.maxsize else alist[dist]

print(dfs(n,times,src, dist))