# https://www.acmicpc.net/problem/18405

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

mapInfor = [ [0] * N for _ in range(N)]
virusInfor = []

for y in range(N):
    a = list(map(int, input().split()))
    for x in range(N):
        mapInfor[y][x] = a[x]
        if a[x] != 0:
            virusInfor.append((a[x],0,y,x))

S, X, Y = map(int, input().split())

virusInfor = sorted(virusInfor)

dx = [1, -1 , 0, 0]
dy = [0, 0, -1, 1]

# q = deque([])
# for virus in virusInfor:
#     q.append([virus[0],virus[0],virus[1], virus[2]])

q = deque(virusInfor)

while q:
    value, timeCount, y, x = q.popleft()

    if timeCount == S:
        break

    for i in range(4):
        yy , xx = y + dy[i], x + dx[i]
        if yy >= 0 and yy < N and xx >= 0 and xx < N:
            if mapInfor[yy][xx] == 0:
                mapInfor[yy][xx] = value
                q.append([value, timeCount + 1, yy, xx])

    # if value == K:
    #     timeCount += 1
    # if timeCount == S:
    #     return mapInfor[X-1][Y-1]


print(mapInfor[X-1][Y-1])
# print(mapInfor)

