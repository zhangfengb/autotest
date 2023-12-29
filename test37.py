"""没有回文子串"""

k =int(input())
s = input()

def dfs(arr,level,flag,maxI,res):
    if level == len(arr):
        return ''.join(map(lambda x:chr(x),res))
    minI = arr[level] if flag else 97
    for i in range(minI,maxI+1):
        if flag and level == len(arr) -1 and minI == i:
            continue
        if level >= 1 and i == res[level - 1]:
            continue
        if level >= 2 and i == res[level -2]:
            continue
        res.append(i)
        ans = dfs(arr,level+1,flag and minI == i,maxI,res)
        if ans is not None:
            return ans
        res.pop()
def getResult():
    arr = list(map(lambda x:ord(x),list(s)))
    maxI = 97 + k - 1
    res=[]
    ans = dfs(arr,0,True,maxI,res)
    print(res)
    if ans:
        return ans
    else:
        return "NO"
print(getResult())