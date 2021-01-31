# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2

# 0 4 8 6
# 3 0 7 9
# 5 9 0 4
# 7 11 2 0

import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
INF = int(1e9)
graph = [[INF] * (N+1) for _ in range(N+1)]

for _ in range(M):
    startNode, endNode, value = map(int,input().split())
    graph[startNode][endNode] = value

for y in range(1,N+1):
    for x in range(1,N+1):
        if x == y:
            graph[y][x] = 0


for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for y in range(1,N+1):
    for x in range(1,N+1):
        print("%d " %graph[y][x], end="")
    print("")