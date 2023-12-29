"""s = input()

def dfs(string):
    temp = []
    fflag = ''
    res = 0

    for i in range(len(string)):
        if '0'<= string[i]<='9':
            if fflag:
                temp.append(string[i])
            else:
                res += int(string[i])
        else:
            if fflag:
                res -= int(''.join(temp))
                temp.clear()
                fflag = ''

            if string[i] == '-':
                fflag = '-'
    print(res)
    return res

dfs(s)"""


n = int(input())
arr = input().split()

def dfs(n,arr,temp,res,used):
    if len(temp) == n:

        str1 = "".join(temp)
        if str1 not in res:
            print(str1)
            res.append(str1)
            return
    for i in range(n):

        if not used[i]:
            temp.append(arr[i])
            used[i] = True
            dfs(n,arr,temp,res,used)
            used[i] = False
            temp.pop()

dfs(n,arr,[],[],[False]*n)

