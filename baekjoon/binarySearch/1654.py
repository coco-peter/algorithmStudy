# 28m

import sys

input = sys.stdin.readline

K, N = map(int,input().split())

numList = []

for _ in range(K):
    numList.append(int(input()))

cnt = 0
start = 1
end = max(numList)
maxValue = 0
maxCnt = 0
while start <= end:

    mid = (start + end) // 2
    cutList = []
    for i in numList:
        cutList.append(i // mid)
    sumValue = sum(cutList)
    # print(mid, sumValue)
    if sumValue < N:
        end = mid -1
    elif sumValue >= N:
        start = mid + 1
        if maxCnt < mid:
            maxCnt = mid


print(maxCnt)
# print(sumValue)