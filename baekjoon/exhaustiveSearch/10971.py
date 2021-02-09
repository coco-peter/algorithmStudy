import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

graph = [[0] * (N) for _ in range(N)]
cityNum = [i for i in range(N)]


for y in range(N):
    numList = list(map(int,input().split()))
    for x in range(N):
        graph[y][x] = numList[x]

candidates = permutations(cityNum, N)

minValue = int(1e9)


def searchMinCost(candidate):
    tempValue = 0
    for i in range(N-1):
        if graph[candidate[i]][candidate[i+1]] != 0:
            tempValue += graph[candidate[i]][candidate[i+1]]
        else:
            return -1
    if graph[candidate[-1]][candidate[0]] != 0:
        tempValue += graph[candidate[-1]][candidate[0]]
    else:
        return -1

    return tempValue

for candidate in candidates:

    tempValue = searchMinCost(candidate)

    if tempValue != -1:
        minValue = min(minValue, tempValue)

print(minValue)