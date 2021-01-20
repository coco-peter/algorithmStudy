# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2


import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

INF = int(1e9)
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    startNode, endNode = map(int, input().split())
    graph[startNode].append((endNode,1))
    graph[endNode].append((startNode, 1))

start = 1
q = []
heapq.heappush(q,(0,start))
distance[1] = 0

while q:
    value, node = heapq.heappop(q)

    if distance[node] < value:
        continue

    for k in graph[node]:
        dist = value + k[1]
        if distance[k[0]] > dist:
            distance[k[0]] = dist
            heapq.heappush(q,(dist,k[0]))

print(distance)
maxValue = max(distance[1:])
count = 0
maxNode = int(1e9)
for i in range(1,len(distance)):
    if distance[i] == maxValue:
        count += 1
        if maxNode > i:
            maxNode = i

print(maxNode,maxValue,count)
