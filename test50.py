n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

def gerResult():
    newList = list(map(lambda x:[x[0],x[0]+x[1]],arr))

    newList.sort(key = lambda y:y[1])
    count = 1
    aa = newList[0][1]
    for i in range(1,len(newList)):
        kai,zhong = newList[i]
        if aa + 15 <= kai:
            count += 1
            aa = zhong

    return count

print(gerResult())