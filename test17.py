import re

s= input()

def dfs(s):

    # reg = re.compile(r"(\d+\.？\d*)")
    alist = re.findall(r"\d+\.？\d*",s)
    print(alist)





print(dfs(s))