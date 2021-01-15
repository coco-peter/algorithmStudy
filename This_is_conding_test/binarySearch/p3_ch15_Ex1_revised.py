# 7 2
# 1 1 2 2 2 2 3

from bisect import bisect_left, bisect_right

N, X = map(int, input().split())

numList = list(map(int, input().split()))

def checkCountTarget(numList, leftValue, rightValue):

    rightIndex = bisect_right(numList, rightValue)
    leftIndex = bisect_left(numList, leftValue)

    print(rightIndex)
    print(leftIndex)
    return rightIndex - leftIndex

count = checkCountTarget(numList, X, X)

if count == 0:
    print(-1)
else:
    print(count)