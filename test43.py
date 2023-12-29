import re

s = input()

"""二叉树中序遍历"""

def gerResule():
    stack = []
    indx = []

    for c in s:
        if c == '{':
            indx.append(len(stack))

        elif c == '}':
            i = indx.pop()
            root = stack[i - 1]
            left,right = '',''
            tem = ''.join(stack[i+1:len(stack)]).split(',')
            print(tem)
            if len(tem) == 1:
                left = tem[0]
            else:
                left,right = tem
            stack = stack[:i-1]
            stack.append(left+root+right)
            continue

        stack.append(c)
#a{b{d,e{g,h{,i}}},c{f}}
    print(stack[0])

gerResule()