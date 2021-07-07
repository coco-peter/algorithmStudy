# 10m

import sys

input = sys.stdin.readline

N, M = map(int,input().split())

treeList = list(map(int,input().split()))

start = 1
end = max(treeList)
maxCnt = 0
maxValue = 0
while start <= end:

    mid = (start + end) // 2
    cutList = []
    for i in treeList:
        if i > mid:
            cutList.append(i - mid)
        else:
            cutList.append(0)

    cutLength = sum(cutList)
    # print(cutLength, M, maxValue,mid)
    if cutLength >= M:
        start = mid + 1
        if maxValue < mid:
            maxValue = mid
    else:
        end = mid - 1

print(maxValue)