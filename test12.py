""" 最短路径"""
import sys

yuan = input()
mub = input()

def helpdef(index,mub,dict1,temp,res):
    if len(temp) == len(mub):
        print('lao')
        dis = temp[0]
        for i in range(1,len(temp)):
            dis += abs(temp[i] - temp[i-1])
        res[0] = min(res[0],dis)
        return res
    for i in range(index,len(mub)):
        indxs = dict1[mub[i]]
        for indx in indxs:
            temp.append(indx)
            helpdef(i+1,mub,dict1,temp,res)
            temp.pop()

def dfs():
    dict1 = {}
    mubs = list(set(mub))
    for i in range(len(yuan)):
        c = yuan[i]
        if c in mubs:
            if c not in dict1.keys():
                dict1[c] = []
            dict1[c].append(i)
    print(dict1)
    res = [sys.maxsize]
    helpdef(0,mub,dict1,[],res)

    return res[0] + 1

print(dfs())