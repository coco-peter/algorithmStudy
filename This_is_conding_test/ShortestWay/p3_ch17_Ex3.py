# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4


import sys
import heapq

T = int(input())
i = 0
while i <= T:
    n = int(input())
    INF = int(1e9)
    graph = [[0] * n for _ in range(n)]
    distance = [ [INF] * (n) for _ in range(n) ]


    for y in range(n):
        valueList = list(map(int, input().split()))
        for x in range(n):
            graph[y][x] = valueList[x]

    startY, startX = 0, 0
    q = []
    heapq.heappush(q,(graph[0][0],startY,startX))
    distance[0][0] = graph[0][0]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        value, nodeY, nodeX = heapq.heappop(q)

        if distance[nodeY][nodeX] < value:
            continue

        for i in range(4):

            nextY, nextX = nodeY + dy[i], nodeX + dx[i]
            if nextY < n and nextY >= 0 and nextX < n and nextX >= 0:
                dist = value + graph[nextY][nextX]
                # print(nodeY,nodeX, nextY,nextX,distance[nextY][nextX], dist, distance[nodeY][nodeX], graph[nextY][nextX])
                if distance[nextY][nextX] > dist:
                    distance[nextY][nextX] = dist
                    heapq.heappush(q,(dist,nextY,nextX))
            # for y in range(n):
            #     for x in range(n):
            #         print("%d " % distance[y][x], end='')
            #     print("")


    print(distance[n-1][n-1])