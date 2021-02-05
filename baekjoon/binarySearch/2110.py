import sys

input = sys.stdin.readline

N, C = map(int,input().split())

houseList = []
for _ in range(N):
    houseList.append(int(input()))

houseList = sorted(houseList)

start = 0
end = len(houseList)

startToMid = -1
midToEnd = -1
res = 0
while start <= end:
    mid = (start + end) // 2

    startToMid = abs(houseList[mid] - houseList[0])
    midToEnd = abs(houseList[len(houseList)-1] - houseList[mid]

    if startToMid == midToEnd:
        res = startToMid
        break
    elif 