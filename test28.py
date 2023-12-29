arr = list(map(int,input().split()))

def dfs():
    num = 1
    for i in range(arr[1]):
        num*=26
    res = 0
    if num >= arr[0]:
        return 1
    else:
        while True:
            num *= 10
            res += 1
            if num >= arr[0]:
                break

    return res

print(dfs())