import sys

input = sys.stdin.readline

N, M = map(int,input().split())


numListA = (list(map(int,input().split())))
numListB = (list(map(int,input().split())))
numList = numListA + numListB


def quickSort(numList, start, end):

    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if numList[left] < numList[pivot] and left <= len(numList) -1:
            left += 1
        if numList[right] > numList[pivot] and right > 0:
            right -= 1

        if left > right:
            numList[pivot], numList[right] = numList[right], numList[pivot]
        else:
            numList[left], numList[right] = numList[right], numList[left]

    quickSort(numList, start, right -1)
    quickSort(numList,right + 1, end)

# quickSort(numList,0, len(numList)-1)

# sorted는 quickSort기반이 아닌 timsort기반이다??
# 둘다 nlogN의 시간복잡도 이지만 최악의 계산량 또한 nlogn이다..??
# 흠..
answer = ' '.join(map(str,sorted(numList)))
print(answer)