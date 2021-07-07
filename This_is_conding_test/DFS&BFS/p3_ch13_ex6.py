# https://www.acmicpc.net/problem/16234

from collections import deque


N, L, R = map(int, input().split())

mapPeople = [[0] * N for _ in range(N)]
checkMoving = 0

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for y in range(N):
    mapPeople[y][:] = list(map(int, input().split()))

# print(mapPeople)
def bfs(y,x,index):

    united = []
    united.append((y,x))

    q = deque([(y,x)])
    isVisited[y][x] = index
    summary = mapPeople[y][x]
    count = 1
    while q:
        pop_y , pop_x = q.popleft()

        for i in range(4):
            yy, xx = pop_y + dy[i], pop_x + dx[i]
            if yy < N and yy >= 0 and xx < N and xx >= 0 and isVisited[yy][xx] == -1:
                if L <= abs(mapPeople[yy][xx] - mapPeople[pop_y][pop_x]) <= R:
                    q.append((yy,xx))
                    isVisited[yy][xx] = index
                    summary += mapPeople[yy][xx]
                    count += 1
                    united.append((yy,xx))

    for y,x in united:
        mapPeople[y][x] = summary // count


while True:

    isVisited = [[-1] * N for _ in range(N)]
    index = 0
    for y in range(N):
        for x in range(N):
            if isVisited[y][x] == -1:
                bfs(y,x, index)
                index += 1


    if index == N * N:
        break

    checkMoving += 1

print(checkMoving)


