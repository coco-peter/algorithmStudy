import sys


input = sys.stdin.readline

R , C = map(int,input().split())

graph = [list(input().rstrip()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

isVisited = [[0] * C for _ in range(R)]

res = 0
def dfs(x, y, history):
    global res
    # print(x, y, cnt, check, history, graph[y][x])
    check = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < C and 0 <= ny < R and graph[ny][nx] not in history:
            dfs(nx,ny, history + graph[ny][nx])
        else:
            check += 1

    if check == 4:
        res = max(res, len(history))
        return

dfs(0, 0, graph[0][0])
print(res)
