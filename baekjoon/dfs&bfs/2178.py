import sys
from collections import deque

input = sys.stdin.readline

h, w = map(int,input().split())

graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    q = deque([(x,y)])

    while q:
        nodeX, nodeY = q.popleft()
        for i in range(4):
            nextX, nextY = nodeX + dx[i] , nodeY + dy[i]
            if 0 <= nextX < w and 0 <= nextY < h:
                if graph[nextY][nextX] == 1:
                    graph[nextY][nextX] = graph[nodeY][nodeX] + 1
                    q.append((nextX,nextY))



for _ in range(h):
    numList = list(map(int,input().strip()))
    graph.append(numList)

bfs(graph,0,0)

print(graph[h-1][w-1])

