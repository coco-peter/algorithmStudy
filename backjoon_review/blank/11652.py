# 1s 256MB

import sys

input = sys.stdin.readline

N = int(input())

numList = []

for _ in range(N):
    numList.append(int(input()))

numList = sorted(numList)

maxNum = numList[0]
cnt = 1
maxCount = 1
for i in range(N-1):


    if numList[i+1] != numList[i]:
        cnt = 1
    else:
        cnt += 1

    if cnt > maxCount:
        maxCount = cnt
        maxNum = numList[i]

    # print(numList[i], cnt, preCnt)

print(numList)
print(maxNum)