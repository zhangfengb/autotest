"""高矮个"""

def dfs(slist):
    flag = True

    for i in range(len(slist)-1):
        if slist[i] != slist[i+1] and (slist[i] > slist[i+1]) != flag:
            slist[i],slist[i+1] = slist[i+1],slist[i]

        flag = not flag

    return " ".join(map(str,slist))

try:
    slist = list(map(int,input().split()))
    # print(slist)

    print(dfs(slist))
except ValueError:
    print('[]')