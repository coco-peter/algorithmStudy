# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2


# [1000000000, 0, 2, 3, 1, 2, 4]

# 03/27 다익스트라 복습
import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
start = int(input())
INF = int(1e9)

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for i in range(M):
    startNode, endNode, value = map(int,input().split())
    graph[startNode].append((value, endNode))


def dijkstra(start):

    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0

    while q:
        value, nowNode = heapq.heappop(q)

        if distance[nowNode] < value :
            continue

        for k in graph[nowNode]:
            dist = k[0] + distance[nowNode]

            if distance[k[1]] > dist:
                distance[k[1]] = dist
                heapq.heappush(q,(dist,k[1]))

dijkstra(start)

for i in range(1, N+1):
    if distance[i] == INF:
        print("can't reach")
    else:
        print(distance[i], end= " ")