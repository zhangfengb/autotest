import math
import sys

n = int(input())
arr = [int(input()) for _ in range(n)]

def getResult():
    hezi = 1474560 // 512
    print(hezi)
    shiyong = []
    langfei = []
    for a in arr:
        shiyong.append(math.ceil(a/512))
        langfei.append(512-a%512)

    sumL = sys.maxsize

    print(langfei)

    print(shiyong)
    for i in range(len(arr)-1):
        sumY = shiyong[i]
        for j in range(i+1,len(arr)):
            sumY += shiyong[j]
            if sumY > hezi:
                print('a')
                hy = sum(shiyong[i:j])

                lang = (hezi-hy) * 512 + sum(langfei[i:j])

                sumL = min(sumL,lang)
                break
            if j == len(arr)-1:
                hy = sum(shiyong[i:j])
                lang = (hezi - hy) * 512 + sum(langfei[i:j])
                sumL = min(sumL, lang)
    return 1474560 - sumL

print(getResult())