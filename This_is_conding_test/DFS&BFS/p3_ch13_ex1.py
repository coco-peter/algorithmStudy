# https://www.acmicpc.net/problem/18352

import sys
from collections import deque

input = sys.stdin.readline
N, M, K, X = map(int, input().split())

INF = int(1e9)
graph = [[] for _ in range(N+1)]
isVisited = [False] * (N+1)
distance = [-1] * (N+1)
distance[X] = 0

for i in range(M):
    startNode, endNode = map(int, input().split())
    graph[startNode].append(endNode)

q = deque([X])
isVisited[X] = True
while q:

    popNode = q.popleft()
    for i in graph[popNode]:
        if isVisited[i] == False:
            isVisited[i] = True
            q.append(i)
            distance[i] = distance[popNode] + 1

# 흠... 왜인지는 모르겠지만 dfs는 recursive error 발생한다. 예제는 통과했는데.. 쩝
# def dfs(startNode, distance, graph, count):
#     # isVisited[startNode] = 1
#     count += 1
#     for i in graph[startNode]:
#
#         if distance[i] > count:
#             distance[i] = count
#         dfs(i, distance, graph, count)
#
#
# distance[X] = 0
# dfs(X, distance, graph, count)

isthereK = False
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        isthereK = True

if isthereK == False:
    print("-1")



# print(distance)
