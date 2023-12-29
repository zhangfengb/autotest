n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

def getResult():
    arr.sort(key = lambda x:(x[0],x[1]))

    stack = [arr[0]]
    temp = [0,0]
    for i in range(1,len(arr)):
        x,y = arr[i]
        if x > stack[-1][1]:
            if temp:
                stack.append(temp[:])
                temp = [0,0]
            else:
                return 'Error'
        if x < stack[-1][1] and y >stack[-1][1]:
            if temp is None:
                temp[0] = x
                temp[0] = y
            elif y > temp[1]:

                temp[0] = x
                temp[1] = y
                if i == len(arr) - 1:
                    stack.append([x,y])

    return len(stack)

print(getResult())







