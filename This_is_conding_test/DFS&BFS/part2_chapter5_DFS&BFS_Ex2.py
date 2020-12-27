# 5 6
# 1 0 1 0 1 0
# 1 1 1 1 1 1
# 0 0 0 0 0 1
# 1 1 1 1 1 1
# 1 1 1 1 1 1

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

from collections import deque

N, M = map(int, input().split())

# mapArray = [[0 for cols in range(M)] for rows in range(N)]
# for i in range(0,N):
#     mapArray[i][:] = map(int, input().split())

# split은 구분을 나누어서 입력을 받는거다.
# 따라서 구분이 없는 데이터를 입력받으려면 아래와 같이 사용하자.
mapArray = []
for i in range(0,N):
    mapArray.append(list(map(int, input())))

# 다시 생각해보면 굳이 방무여부를 판단하는 배열을 굳이 안만들어도 되는 경우가 있으니 잘 판단해서 코드를 작성하자.
isVisited = [[0 for cols in range(M)] for rows in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(startNodeX,startNodeY ):
    # 상하좌우

    queue = deque([(startNodeX,startNodeY)])
    isVisited[startNodeY][startNodeX] = 1

    while queue:
        popNodeX, popNodeY = queue.popleft()


        for i in range(0,4):
            x, y = popNodeX + dx[i], popNodeY + dy[i]
            if x >= 0 and x < M and y >= 0 and y < N:
                if mapArray[y][x] == 1 and isVisited[y][x] == 0:
                    mapArray[y][x] = mapArray[popNodeY][popNodeX] + 1
                    isVisited[y][x] = 1
                    queue.append((x,y))

    return mapArray[N-1][M-1]


print(bfs(0,0))
