k = int(input())
s = input()
# paswd_"asd_fjgn"_jng_""_
def dfs(k,s):
    stack = []
    res = []

    for c in s:
        if c == '_' and (len(stack) == 0 or stack[0] != '"'):
            res.append("".join(stack))
            stack.clear()
        elif c == '"' and len(stack) != 0:
            stack.append(c)
            res.append("".join(stack))
            stack.clear()
        else:
            stack.append(c)

    if len(stack)!=0:
        res.append("".join(stack))

    ans = list(filter(lambda x:x != "",res))

    if k >= len(ans):
        return 'ERROR'

    ans[k] = '******'

    return "_".join(ans)

print(dfs(k,s))