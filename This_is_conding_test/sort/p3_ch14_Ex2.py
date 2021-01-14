# https://www.acmicpc.net/problem/18310

N = int(input())

a = list(map(int, input().split()))

a = set(a)

minValue = int(1e9)
shortestPosition = 0
for i in a:
    curPos = i
    distance = 0

    for j in a:
        eachDistance = abs(curPos - j)
        distance += eachDistance

    if minValue > distance:
        minValue = distance
        shortestPosition = i

print(shortestPosition)
print(minValue)


