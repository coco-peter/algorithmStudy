import sys
from collections import deque

input = sys.stdin.readline


M, N = map(int,input().split())

graph = [ [0] * M for _ in range(N)]

q = deque()

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

for y in range(N):
    numList = list(map(int,input().split()))
    for x in range(M):
        graph[y][x] = numList[x]
        if numList[x] == 1:
            q.append((x,y))

while q:
    nodeX, nodeY = q.popleft()

    for i in range(4):
        nx, ny = nodeX + dx[i],  nodeY + dy[i]
        if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 0:
            q.append((nx, ny))
            graph[ny][nx] = graph[nodeY][nodeX] + 1

maxValue = -1
isPossible = True
for y in range(N):
    # print(graph[y][:])
    for x in range(M):
        maxValue = max(maxValue, graph[y][x])
        if graph[y][x] == 0:
            isPossible = False

if isPossible:
    print(maxValue - 1)
else:
    print(-1)