""" 英文输入法 """
import re

s= input()
pre = input()

def dfs(s,pre):
    tem = re.split("[^a-zA-Z]",s)
    list1 = list(set(tem))
    list1.sort()
    list1 = list(filter(lambda x:x.startswith(pre),list1))
    if len(list1) > 0:
        return " ".join(list1)
    else:
        return pre

print(dfs(s,pre))