# https://www.acmicpc.net/problem/14502


# 뭐지 분명 시간초과가 날줄 알았는데 통과 했네??
# 나중에 시간을 줄이는 방법을 한번 고민해보자

from itertools import combinations
from collections import deque
import sys
import copy
import time




start = time.time()
input = sys.stdin.readline
N, M = map(int, input().split())

mapInfor = [ [0] * M for _ in range(N)]     # N * M
zeroInfor = []
twoInfor = []

for y in range(N):
    a = list(map(int, input().split()))
    for x in range(M):
        mapInfor[y][x] = a[x]
        if a[x] == 0:
            zeroInfor.append((y,x))
        elif a[x] == 2:
            twoInfor.append((y,x))


candidates = list(combinations(zeroInfor,3))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

maxValue = 0

for candidate in candidates:
    tempMapInfor = copy.deepcopy(mapInfor)
    count = 0
    for i in range(3):
        tempMapInfor[candidate[i][0]][candidate[i][1]] = 1

    q = deque([])
    for virus in twoInfor:
        q.append([virus[0],virus[1]])

    while q:
        y, x = q.popleft()

        for i in range(4):
            yy , xx = y + dy[i] , x + dx[i]
            if xx >= 0 and yy >=0 and xx < M and yy < N and tempMapInfor[yy][xx] != 1 and tempMapInfor[yy][xx] != 2:
                if tempMapInfor[yy][xx] == 0:
                    tempMapInfor[yy][xx] = 2
                    q.append([yy,xx])

    for y in range(N):
        for x in range(M):
            if tempMapInfor[y][x] == 0:
                count += 1

    if count > maxValue:
        maxValue = count

print(maxValue)

# for y in range(N):
#     print(tempMapInfor[y][:])

# print("time: ", time.time() - start)