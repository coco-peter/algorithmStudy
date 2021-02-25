import sys
from collections import deque
import copy

input = sys.stdin.readline

R, C = map(int,input().split())

graph = [[0] * C for _ in range(R)]

for y in range(R):
    graph[y][:] = list(input().strip())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = 0
def dfs(x, y, history):
    global res

    isPossible = 0
    # print(history)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < C and 0 <= ny < R and graph[ny][nx] not in history:
            dfs(nx, ny, history + graph[ny][nx])
        else:
            isPossible += 1

    if isPossible == 4:
        res = max(res, len(history))
        return

dfs(0,0,graph[0][0])
print(res)