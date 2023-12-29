arr = list(map(int,input().split(',')))
n = int(input())

def getResult():
    arr.sort()
    if n >= len(arr):
        return 0
    if n >= len(arr)-n:
        return arr[len(arr)-n-1]

    num = arr[0:n]
    for i in range(n):
        arr.pop()
    for i in range(n,len(arr),n):
        xinarr = arr[n:n+n]
        print(xinarr)
        for j in range(len(xinarr)-1,-1,-1):
            duan = min(num)
            idx = num.index(duan)
            num[idx] += xinarr[j]
    print(num)


    return max(num)

print(getResult())
