"""翻牌"""
arr = list(map(int,input().split()))

def dfs():

    temp =[0]*len(arr)
    temp[0] = arr[0]
    for i in range(1,len(arr)):
        if i < 3:
            if arr[i] + temp[i-1] < 0:
                temp[i] = 0
            else:
                temp[i] = arr[i] + temp[i-1]

        else:
            if arr[i] + temp[i-1] > temp[i - 3]:
                temp[i] = arr[i] + temp[i-1]
            else:
                temp[i] = temp[i - 3]

    return temp[-1]

print(dfs())
