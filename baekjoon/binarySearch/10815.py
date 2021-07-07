import sys

input = sys.stdin.readline

N = int(input())
cardList = list(map(int,input().split()))

M = int(input())
checkList = list(map(int,input().split()))

cardList = sorted(cardList)

# print(cardList)
def binarySearch(start, end, target):

    if start > end:
        return 0

    mid = (start + end) // 2

    if cardList[mid] == target:
        return 1
    elif cardList[mid] > target:
        end = mid - 1
        return binarySearch(start, end, target)
    else:
        start = mid + 1
        return binarySearch(start, end, target)

for i in checkList:

    start, end = 0, len(cardList) -1
    res = binarySearch(start, end, i)
    print("%d " %res, end = "")


