n = int(input())
arr = list(map(int,input().split()))
nl = int(input())

def getResult():
    if len(arr) == 1:
        return 1 if arr[0] >= nl else 0

    arr.sort(reverse=True)
    l = 0
    r = n - 1
    count = 0

    while r>l:
        if arr[l] >= nl:
            l += 1
            count += 1
        elif arr[l] + arr[r] >= nl:
            l += 1
            r -= 1
            count += 1
        else:
            r -= 1

    return count

print(getResult())