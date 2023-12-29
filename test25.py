slite = input().split()

def dfs():
    arr = []
    for student in slite:
        s = student.split("/")
        ind = s[0]
        ist = s[1]

        if int(ind) < 0 or int(ind) > 999:
            return 'ERROR'

        arr.append(ist)

    ban1 = [True]*len(arr)


    for i in range(1,len(arr)):
        if arr[i] == "N":
            ban1[i] = not ban1[i-1]
        else:
            ban1[i] = ban1[i-1]
    print(ban1)
    one = []
    two = []
    for j in range(len(ban1)):
        if ban1[j]:
            one.append(j+1)
        else:
            two.append(j+1)
    print(one)
    print(two)
    print(" ".join(map(str,one)))
    print(" ".join(map(str,two)))

dfs()

