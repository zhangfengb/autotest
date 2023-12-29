import re

s = input()

def dfs(s):
    reg1 = '[^0-9a-zA-Z\-]'
    alist = re.split(reg1,s)
    print(alist)


dfs(s)