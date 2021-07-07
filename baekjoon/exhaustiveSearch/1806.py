import sys

input = sys.stdin.readline

N, M = map(int,input().split())

numList = list(map(int, input().split()))


low, high = 0, 1
temp = numList[low]
# dist = int(1e9)
dist = sys.maxsize

while low < N:
    if temp >= M:
        dist = min(dist, high - low)
        temp -= numList[low]
        low += 1

        if temp < M and high < N:
            temp += numList[high]
            high += 1
    else:
        if high >= N:
            break

        temp += numList[high]
        high += 1

        if high - low >= dist:
            temp -= numList[low]
            low += 1

print(dist)