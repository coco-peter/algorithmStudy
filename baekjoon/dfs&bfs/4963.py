from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1,-1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]


def bfs(graph, x, y, isVisited):
    q = deque([(x,y)])
    isVisited[y][x] = True

    while q:
        nodeX, nodeY = q.popleft()

        for i in range(8):
            nextX, nextY = nodeX + dx[i] , nodeY + dy[i]
            if nextX >= 0 and nextX < w and nextY >=0 and nextY < h:
                if isVisited[nextY][nextX] == False and graph[nextY][nextX] == 1:
                    isVisited[nextY][nextX] = True
                    q.append((nextX,nextY))


while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0 :
        break
    graph = [[0] * w for _ in range(h)]
    isVisited = [[False] * w for _ in range(h)]

    for y in range(h):
        numList = list(map(int,input().split()))
        for x in range(w):
            graph[y][x] = numList[x]

    islandCount = 0
    for y in range(h):
        for x in range(w):
            if isVisited[y][x] == False and graph[y][x] == 1:
                bfs(graph, x, y, isVisited)
                islandCount += 1

    print(islandCount)




