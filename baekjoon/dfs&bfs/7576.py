import sys
from collections import deque

input = sys.stdin.readline

w, h = map(int,input().split())
graph = [[0] * w for _ in range(h)]
# isVisited = [[False] * w for _ in range(h)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

for y in range(h):
    numList = list(map(int, input().split()))
    for x in range(w):
        graph[y][x] = numList[x]
        if numList[x] == 1:
            q.append((x,y))

while q:
    nodeX,nodeY = q.popleft()

    for i in range(4):
        nextX, nextY = nodeX + dx[i], nodeY + dy[i]
        if nextX >= 0 and nextX < w and nextY >=0 and nextY < h:
            if graph[nextY][nextX] == 0:
                graph[nextY][nextX] = graph[nodeY][nodeX] + 1
                q.append((nextX, nextY))

# print(graph)
isPossible = True
cnt = 0
for y in range(h):
    for x in range(w):
        if graph[y][x] == 0:
            print("-1")
            isPossible = False
        if cnt < graph[y][x]: cnt = graph[y][x]

if isPossible:
    print(cnt-1)