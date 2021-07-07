# 5
# 8 3 7 9 2
# 3
# 5 7 9

# NO , Yes, Yes


import sys

input = sys.stdin.readline

N = int(input())
numList = map(int, input().split())
M = int(input())
targetList = map(int, input().split())


def binarySearch(start, end, target):

    if start > end:
        return None

    mid = (start + end) // 2

    if numList[mid] == target:
        return mid
    elif numList[mid] < target:
        return binarySearch(mid + 1, end, target)
    elif numList[mid] > target:
        return binarySearch(start, mid - 1 , target)


numList = sorted(numList)

for i in targetList:

    result = binarySearch(0, len(numList) -1, i)
    if result != None:
        print("Yes")
    else:
        print("NO")