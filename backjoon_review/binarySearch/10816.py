import sys

input = sys.stdin.readline

N = int(input())
cardList = list(map(int,input().split()))
M = int(input())
targetList = list(map(int,input().split()))

cardList = sorted(cardList)

def binarySearchFirst(start, end, target):
    if start > end:
        return -1

    mid = (start + end) // 2

    if cardList[mid] == target:
        if mid == 0:
            return mid
        else:
            if cardList[mid] > cardList[mid - 1]:
                return mid
            else:
                return binarySearchFirst(start, mid -1, target)
    elif cardList[mid] > target:
        return binarySearchFirst(start, mid - 1, target)
    elif cardList[mid] < target:
        return binarySearchFirst(mid + 1, end, target)


def binarySearchEnd(start, end, target):
    if start > end:
        return -1

    mid = (start + end) // 2

    if cardList[mid] == target:
        if mid == len(cardList) - 1:
            return mid
        else:
            if cardList[mid] < cardList[mid + 1]:
                return mid
            else:
                return binarySearchEnd(mid + 1, end, target)
    elif cardList[mid] > target:
        return binarySearchEnd(start, mid - 1, target)
    elif cardList[mid] < target:
        return binarySearchEnd(mid + 1, end, target)


# print(cardList)
for i in range(M):
    firstIndex = binarySearchFirst(0, len(cardList) -1, targetList[i])

    if firstIndex != -1:
        endIndex = binarySearchEnd(0, len(cardList) -1 , targetList[i])
        # print(endIndex, firstIndex, targetList[i], endIndex - firstIndex + 1)
        print(endIndex - firstIndex + 1, end = " ")
    else:
        # print(endIndex, firstIndex, targetList[i], 0)
        print(0, end = " ")

