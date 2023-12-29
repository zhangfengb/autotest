s = input()

def dfs(s):
    res = 0

    i = 0
    j = 0

    while i < len(s):
        if '0'<= s[i]<='9':
            if i != j:
                if s[i]>=s[i-1]:
                    res = max(res, i - j)
                    i += 1
                else:
                    res = max(res, i - j)

                    j = i
                    i += 1
            else:
                res = max(res, 1)
                i += 1
        else:
            res = max(res,i-j)
            i += 1
            j = i

    return res

print(dfs(s))