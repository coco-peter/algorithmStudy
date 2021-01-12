# https://www.acmicpc.net/problem/18428

from itertools import combinations
import copy

N = int(input())

mapInfor = [[] * N for _ in range(N)]

obstacleInfor = []
teacherInfor = []

dx = [1, -1 , 0, 0]
dy = [0, 0, -1, 1]


def isthereStudent(y, x):

    for i in range(4):
        temp_y, temp_x = y, x
        if i == 0:                  # 동
            while temp_x < N - 1:
                temp_y, temp_x = temp_y + dy[i], temp_x + dx[i]
                if tempMapInfor[temp_y][temp_x] == "O":
                    break
                elif tempMapInfor[temp_y][temp_x] == "S":
                    return True
        if i == 1:                  # 서
            while temp_x >= 1:
                temp_y, temp_x = temp_y + dy[i], temp_x + dx[i]
                if tempMapInfor[temp_y][temp_x] == "O":
                    break
                elif tempMapInfor[temp_y][temp_x] == "S":
                    return True
        if i == 2:                  # 남
            while temp_y >= 1:
                temp_y, temp_x = temp_y + dy[i], temp_x + dx[i]
                if tempMapInfor[temp_y][temp_x] == "O":
                    break
                elif tempMapInfor[temp_y][temp_x] == "S":
                    return True
        if i == 3:                  # 북
            while temp_y < N - 1:
                temp_y, temp_x = temp_y + dy[i], temp_x + dx[i]
                if tempMapInfor[temp_y][temp_x] == "O":
                    break
                elif tempMapInfor[temp_y][temp_x] == "S":
                    return True

    return False


for y in range(N):
    mapInfor[y][:] = list(input().split())
    for x in range(N):
        if mapInfor[y][x] == "X":
            obstacleInfor.append((y,x))
        if mapInfor[y][x] == "T":
            teacherInfor.append((y,x))



candidates = combinations(obstacleInfor,3)
checkStudent = False
canFind = False

for candidate in candidates:
    tempMapInfor = copy.deepcopy(mapInfor)
    checkCount = 0
    # print(candidate)
    for i in range(3):
        tempMapInfor[candidate[i][0]][candidate[i][1]] = "O"
        # print(candidate[i][0], candidate[i][1])
    # print(tempMapInfor)
    for teacher in teacherInfor:
        # print(teacher)
        y ,x = teacher[0], teacher[1]

        checkStudent = isthereStudent(y,x)

        if checkStudent == True:
            checkCount += 1

    if checkCount == 0:
        canFind = True
        print("YES")
        break

if canFind == False:
    print("NO")