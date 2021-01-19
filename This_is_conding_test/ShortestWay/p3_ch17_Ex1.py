# https://www.acmicpc.net/problem/11404

import sys

input = sys.stdin.readline


n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF] * (n+1) for _ in range((n+1))]

for y in range(1,(n+1)):
    for x in range(1,(n+1)):
        if x == y:
            graph[y][x] = 0

for i in range(m):
    startNode, endNode, value = map(int, input().split())
    if graph[startNode][endNode] > value:
        graph[startNode][endNode] = value

for i in range(1,(n+1)):
    for j in range(1,(n+1)):
        for k in range(1,(n+1)):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])


for j in range(1,(n+1)):
    for k in range(1,(n+1)):
        if graph[j][k] == INF:
            print("0 ", end="")
        else:
            print("%d "%graph[j][k], end="")
    print("")