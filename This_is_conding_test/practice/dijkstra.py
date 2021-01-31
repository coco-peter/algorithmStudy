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

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
start = int(input())

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    startNode, endNode, value = map(int,input().split())
    graph[startNode].append((endNode,value))

q = []
heapq.heappush(q,(0,start))
distance[start] = 0

while q:
    dist, node = heapq.heappop(q)

    if distance[node] < dist:
        continue

    for k in graph[node]:
        distNew = k[1] + dist
        if distance[k[0]] > distNew:
            distance[k[0]] = distNew
            heapq.heappush(q,(distNew,k[0]))

print(distance)
