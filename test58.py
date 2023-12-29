s = input()

def getResult():
    n = len(s)
    sarr = list(map(lambda c:ord(c),list(s)))

    left = 1
    right = len(sarr) - 2

    while left<right:
        qian = sarr[:left]
        zhong = sarr[left+1:right]
        hou = sarr[right+1:]
        if sum(qian) == sum(zhong) == sum(hou):
            print(str(left)+','+str(right))
            return
            break
        elif sum(qian) > sum(hou):
            right -= 1
        elif sum(qian) < sum(hou):
            left += 1
        else:
            left += 1

    print('0,0')

getResult()



