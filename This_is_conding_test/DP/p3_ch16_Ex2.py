# https://www.acmicpc.net/problem/1932

n = int(input())

mapInfor = [[-1] * n for _ in range(2 * n -1)]

start_y = (2 * n - 1) // 2
start_x = 0
index = 1
for x in range(n):
    numlist = list(map(int, input().split()))
    y_index = start_y
    for y in range(index):
        mapInfor[y_index][x] = numlist[y]
        y_index += 2
    index += 1
    start_y -= 1

for x in range(1,n):
    for y in range(2 * n - 1):
        if mapInfor[y][x] != -1:
            print(mapInfor[y][x])
            if y - 1 < 0:
                left_top = 0
            else:
                if mapInfor[y - 1][x - 1] != -1:
                    left_top = mapInfor[y-1][x-1]
                else:
                    left_top = 0

            if y + 1 >= n:
                left_bottom = 0
            else:
                if mapInfor[y + 1][x - 1] != -1:
                    left_bottom = mapInfor[y+1][x-1]
                else:
                    left_bottom = 0

            mapInfor[y][x] = mapInfor[y][x] + max(left_top, left_bottom)


result = 0
for y in range(2 * n -1):
    result = max(result, mapInfor[y][n-1])


print(result)

for y in range(2*n -1):
    print(mapInfor[y][:])