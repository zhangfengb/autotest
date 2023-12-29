"""按身高体重排序"""
k = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

def dfs():
    res = []
    for i in range(k):
        res.append([arr1[i],arr2[i],i+1])
    print(res)
    res.sort(key=lambda x:(x[0],x[1],x[2]))
    print(res)

    return " ".join(map(lambda x:str(x[2]),res))

print(dfs())



