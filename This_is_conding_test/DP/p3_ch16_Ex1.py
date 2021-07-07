# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2



T = int(input())

for _ in range(T):
    n, m  = map(int, input().split())
    mapInfor = [ [0] * m for i in range(n)]

    numList = list(map(int, input().split()))
    index = 0
    for y in range(n):
        for x in range(m):
            mapInfor[y][x] = numList[index]
            index += 1

    totalMaxValue = 0

    dx = [1, 1, 1]      # 오른쪽, 오른쪽아래, 오른쪽 위
    dy = [0, -1, 1]


    for y in range(n):
        curX , curY = 0, y
        valueSum = mapInfor[curY][curX]
        for x in range(m-1):
            maxValue = 0
            for i in range(3):
                nextX, nextY = curX + dx[i], curY + dy[i]
                if nextY >= 0 and nextY < n:
                    if maxValue < mapInfor[nextY][nextX]:
                        maxValue = mapInfor[nextY][nextX]
                        xx, yy = nextX, nextY
            curX, curY = xx, yy

            valueSum += maxValue

        if totalMaxValue < valueSum:
            totalMaxValue = valueSum

    print("total ", totalMaxValue)
