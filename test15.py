"""最远zuji"""
import re

s = input()


def dfs(s):
    alist = re.findall('(\d+),(\d+)', s)
    res = (0, 0)
    maxjl = 0
    for ii in alist:
        '''blist = list(ii)
        print(blist)'''
        if ii[0][0] == '0' or ii[1][0] == '0':
            continue
        x = int(ii[0])
        y = int(ii[1])
        ji = x * x + y * y
        if ji > maxjl:
            res = '(' + str(x) + ',' + str(y) + ')'

    return res


def dfs1(s):
    count = 0
    patten = re.compile('(^a-z)')
    tag1 = re.compile('[^aeiou][aeiou][^aeiou]e')
    tag2 = re.compile('e[^aeiou][aeiou][^aeiou]')

    alist = s.split()
    for aa in alist:
        if patten.search(aa):
            tag = tag1
        else:
            tag = tag2

        for i in range(len(aa)-3):
            if tag.match(aa[i:i+4]) and aa[i:i+2] != aa[i+2:i+4]:

                count += 1

    return count

print(dfs1(s))
