

# 3/22 백준 1525 복습

import sys
from collections import deque

input = sys.stdin.readline

targetGraph = [[1,2,3], [4,5,6],[7,8,0]]


# 이제 이런식으로 코드를 짜자
# graph = [list(map(int,input().split())) for _ in range(3)]
graph = [[0] * 3 for _ in range(3)]

for y in range(3):
    numList = list(map(int,input().split()))
    for x in range(3):
        graph[y][x] = numList[x]
        if numList[x] == 0:
            startX, startY = x, y



isVisited = [[False] * 3 for _ in range(3)]
isPossible = True





dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, sx, sy, cnt, isVisited):
    global isPossible
    q = deque([(graph, sx, sy, cnt, isVisited)])
    # isVisited[sy][sx] = True
    while q:
        graph, x, y , cnt, isVisited = q.popleft()
        isVisited[y][x] = True
        print(x,y)
        if x == 2 and y == 2:
            isPossible = True
            for y in range(3):
                for x in range(3):
                    if graph[y][x] != targetGraph[y][x]:
                        isPossible = False
                        break
            if isPossible == True:
                return cnt
        cnt += 1
        for i in range(4):
            nx, ny = x + dx[i] , y + dy[i]

            if 0 <= nx < 3 and 0 <= ny < 3 and isVisited[ny][nx] == False:
                graph[ny][nx], graph[y][x] = graph[y][x], graph[ny][nx]
                q.append((graph, nx, ny, cnt, isVisited))



    return -1


print(bfs(graph, startX,startY,0, isVisited))
