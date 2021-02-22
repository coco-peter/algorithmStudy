import sys
from collections import deque
input = sys.stdin.readline


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs1(x, y, color):
    q = deque()
    q.append((x,y))
    isVisited[y][x] = color
    while q:
        nodeX, nodeY = q.popleft()

        for i in range(4):
            nx , ny = nodeX + dx[i], nodeY + dy[i]
            if 0 <= nx < N and 0 <= ny < N and isVisited[ny][nx] == 0 and graph[ny][nx] == 1:
                q.append((nx, ny))
                isVisited[ny][nx] = color

def bfs2(color):
    while q2:
        nodeX, nodeY = q2.popleft()

        for i in range(4):
            nx, ny = nodeX + dx[i], nodeY + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if isVisited[ny][nx] != color and graph[ny][nx] == 1:
                    return isVisited2[nodeY][nodeX] -1
                if isVisited2[ny][nx] == 0 and graph[ny][nx] == 0:
                    isVisited2[ny][nx] = isVisited2[nodeY][nodeX] + 1
                    q2.append((nx, ny))

N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]
isVisited = [[0] * N for _ in range(N)]

cnt = 1
for y in range(N):
    for x in range(N):
        if graph[y][x] == 1 and isVisited[y][x] == 0:
            bfs1(x,y,cnt)
            cnt += 1


answer = sys.maxsize
for i in range(1, cnt):
    q2 = deque()
    isVisited2 = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if graph[y][x] == 1 and isVisited[y][x] == i:
                q2.append((x,y))
                isVisited2[y][x] = 1

    result = bfs2(i)

    answer = min(answer, result)
# print(isVisited2)
print(answer)