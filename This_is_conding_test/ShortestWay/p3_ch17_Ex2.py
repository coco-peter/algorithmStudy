# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4



import sys

input = sys.stdin.readline

N, M = map(int, input().split())
INF = int(1e9)
graph = [ [INF] * (N+1) for _ in range(N+1)]

for y in range(1,N+1):
    for x in range(1,N+1):
        if y == x:
            graph[y][x] = 0


for i in range(M):
    startNode, endNode = map(int, input().split())
    graph[startNode][endNode] = 1


for i in range(1,N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

result = 0
for y in range(1,N+1):
    count = 0
    for x in range(1,N+1):
        if graph[y][x] != INF or graph[x][y] != INF:
            count += 1

    if count == N:
        result +=1

print(result)