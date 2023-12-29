m,n =map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(m)]

def getResult():
    lie = [0] * n
    hang = []
    for i in range(m):
        h = 0
        for j in range(n):
            if arr[i][j] == 0:
                lie[j] += 1
                h += 1
        hang.append(h)

    lie = list(filter(lambda x:x>=int(m/2),lie))
    hang = list(filter(lambda x:x>=int(n/2),hang))

    print(len(lie))
    print(len(hang))

getResult()

