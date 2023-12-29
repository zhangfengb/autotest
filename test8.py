k = input()
s = input()

def dfs():
    set1 = set(k)
    set2 = set(s)

    set3 = set1 & set2

    list1 = list(set3)
    list1.sort()

    return "".join(list1)

print(dfs())