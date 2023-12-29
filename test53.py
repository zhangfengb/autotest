arr = list(map(int,input().split()))

def getResult():
    print(arr)
    left = 1
    right = len(arr) - 2
    zuo = arr[0]
    you = arr[len(arr) - 1]
    while right >= left:

        if zuo == you:
            return left
            break
        elif zuo > you:

            you *= arr[right]

            right -= 1
        else:


            zuo *= arr[left]
            left += 1


    return '-1'

print(getResult())