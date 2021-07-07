import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [[0] * N for _ in range(N)]
color = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(graph, x, y, colorIndex):
    q = deque([(x,y)])
    color[y][x] = colorIndex

    while q:
        nodeX, nodeY = q.popleft()
        for i in range(4):
            nextNodeX , nextNodeY = nodeX + dx[i], nodeY + dy[i]
            if 0 <= nextNodeX < N and 0 <= nextNodeY < N:
                if graph[nextNodeY][nextNodeX] == 1 and color[nextNodeY][nextNodeX] == False:
                    q.append((nextNodeX, nextNodeY))
                    color[nextNodeY][nextNodeX] = colorIndex


def findWay(candidate, graph, graph2, colorIndex):

    while candidate:
        nodeX, nodeY = candidate.popleft()
        for i in range(4):
            nextNodeX , nextNodeY = nodeX + dx[i], nodeY + dy[i]
            if 0 <= nextNodeX < N and 0 <= nextNodeY < N:
                if graph[nextNodeY][nextNodeX] == 1 and color[nextNodeY][nextNodeX] != colorIndex:
                    return graph2[nodeY][nodeX]

                if graph[nextNodeY][nextNodeX] == 0 and graph2[nextNodeY][nextNodeX] == 0:
                    candidate.append((nextNodeX, nextNodeY))
                    graph2[nextNodeY][nextNodeX] = graph2[nodeY][nodeX] + 1


for y in range(N):
    numList = list(map(int, input().split()))
    for x in range(N):
        graph[y][x]= numList[x]

colorIndex = 1
for y in range(N):
    for x in range(N):
        if graph[y][x] == 1 and color[y][x] == False:
            bfs(graph, x, y, colorIndex)
            colorIndex += 1

res = int(1e9)
cost = 0

for i in range(1,colorIndex):
    candidate = deque()
    graph2 = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if graph[y][x] == 1 and color[y][x] == i:
                candidate.append((x,y))
                graph2[y][x] == 1
    cost = findWay(candidate, graph, graph2, i)

    res = min(cost, res)

print(res)


