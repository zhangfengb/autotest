k = int(input())
arr = list(map(int,input().split()))
""" 路灯照不亮的长度"""
def dfs(k,arr):
    res = [[0,arr[0]]]
    for i in range(1,k):
        tem = i*100
        res.append([tem-arr[i],tem+arr[i]])

    res.sort(key=lambda x:x[0])

    xres =[res[0]]
    num = 0
    for j in range(1,k):
        if xres[-1][1] >= res[j][0]:
            xres[-1][1] = max(xres[-1][1],res[j][1])
        else:
            num += (res[j][0]-xres[-1][1])
            xres.append(res[j])

    return num

print(dfs(k,arr))