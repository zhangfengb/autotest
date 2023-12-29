arr = list(map(int,input().split()))


def helps(k,arr,used,temp,group,res):
    if len(group) == sum(arr)/k and sum(group[-1]) == k:
        res.append(len(group))
        return
    for i in range(len(arr)):
        if sum(temp)+arr[i] <= k and not used[i]:
            temp.append(arr[i])
            used[i] = True
            helps(k,arr,used,temp,group,res)
            used[i] = False
            temp.pop()
        if sum(temp) == k:
            group.append(temp[:])
            temp = []

def dfs():
    sumL = sum(arr)
    temp = []
    for i in range(2,sumL):
        if sumL%i == 0:
            temp.append(i)

    minL = max(arr)
    temp = list(filter(lambda x:x>=minL,temp))
    res = []
    for k in temp:
        helps(k,arr,[False]*len(arr),[],[],res)
        if res:
            return res[0]
    
    if res:
        pass
    else:
        return -1

print(dfs())