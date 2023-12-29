import re

arr = input().split(',')

def getResult():
    s = ''
    for aa in arr:
        s += '/'+aa

    s = re.sub(r'/+','/',s)
    return s

print(getResult())