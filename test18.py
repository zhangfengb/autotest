import re

s= input()

def dfs(s):

    alist = re.compile(r'A={(.+)},B={(.+)},C=(.+)').search(s)
    print(alist.group(2))

dfs(s)
