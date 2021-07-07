import sys
from collections import deque
import copy

input = sys.stdin.readline

C, R = map(int,input().split())

graph = [[0] * C for _ in range(R)]

for y in range(R):
    graph[y][:] = list(input().strip())


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

isVisited = [[False] * C for _ in range(R)]
res = sys.maxsize
def dfs(x, y, cnt, history):
    global res

    if x == C - 2 and y == R - 1:
        res = min(res, cnt)
        return
    elif x == C - 1 and y == R - 2:
        res = min(res, cnt)
        return

    history[y][x] = True

    # print(x, y, C, R)
    # print(history)

    cnt += 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # print(nx, ny, graph[ny][nx], history[ny][nx])
        if 0 <= nx < C and 0 <= ny < R and graph[ny][nx] == "1" and history[ny][nx] == False:
            temp = copy.deepcopy(history)
            dfs(nx, ny, cnt, temp)


dfs(0, 0, 0, isVisited)
print(res)
