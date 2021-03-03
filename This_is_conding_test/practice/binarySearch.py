# 5
# 8 3 7 9 2
# 3
# 5 7 9

# NO , Yes, Yes


import sys

input = sys.stdin.readline

N = int(input())

numList = list(map(int, input().split()))

numList = sorted(numList)
M = int(input())
targetList = list(map(int, input().split()))


def binarySearch(start, end, target):

    if start > end:
        return 0

    mid = (start + end) // 2

    if numList[mid] == target:
        return 1
    elif numList[mid] > target:
        return binarySearch(start, mid - 1, target)
    else:
        return binarySearch(mid + 1, end, target)


for i in range(M):
    res = binarySearch(0, len(numList), targetList[i])
    if res:
        print("Yes")
    else:
        print("NO")