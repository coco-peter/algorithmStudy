import sys

input = sys.stdin.readline

N, M = map(int, input().split())

chessMap = [[0] * M for _ in range(N)]
isVisited = [[False] * M for _ in range(N)]
dx = [1, 2, 2, 1]
dy = [-2, -1, 1, 2]

startX , startY = 0, N - 1
moveCnt = 0
def checkMoveCnt(startX, startY):
    global moveCnt
    print(startX, startY)
    isVisited[startY][startX] = True
    if moveCnt < 4:
        for i in range(4):
            nx , ny = startX + dx[i] , startY + dy[i]
            if 0 <= nx < M and 0 <= ny <N and isVisited[ny][nx] == False:
                moveCnt += 1
                checkMoveCnt(nx, ny)
                break
    else:
        for i in range(4):
            nx , ny = startX + dx[i] , startY + dy[i]
            if 0 <= nx < M and 0 <= ny <N and isVisited[ny][nx] == False:
                moveCnt += 1
                checkMoveCnt(nx,ny)

checkMoveCnt(startX,startY)
cnt = 0
for y in range(N):
    for x in range(M):
        if isVisited[y][x] == 1:
            cnt += 1

print(cnt)






