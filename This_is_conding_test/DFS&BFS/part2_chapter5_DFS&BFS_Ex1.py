# 4 5
# 0 0 1 1 0
# 0 0 0 1 1
# 1 1 1 1 1
# 0 0 0 0 0

N, M = map(int, input().split())

mapArray = [[0 for cols in range(M)] for rows in range(N)]

for i in range(0,N):
    mapArray[i][:] = map(int, input().split())

isVisited = [[0 for cols in range(M)] for rows in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

countIceCream = 0

def dfs(mapArray, startNodeX, startNodeY, isVisited):
    # 상하좌우

    isVisited[startNodeY][startNodeX] = 1
    for x in dx:
        for y in dy:
            if startNodeX + x > -1 and startNodeX + x < M and startNodeY + y > -1 and startNodeY + y < N:
                if mapArray[startNodeY + y][startNodeX + x] == 0 and isVisited[startNodeY + y][startNodeX + x] == False:
                    dfs(mapArray, startNodeX + x, startNodeY + y, isVisited)

for posX in range(0,M):
    for posY in range(0,N):
        if mapArray[posY][posX] == 0 and isVisited[posY][posX] == False:        # 아이스크림 틀이면서 방문하지 않은것들만
            dfs(mapArray, posX, posY, isVisited)
            countIceCream += 1

print(countIceCream)
