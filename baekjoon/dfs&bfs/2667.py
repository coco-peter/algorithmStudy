import sys
from collections import deque


# split은 구분을 나누어서 입력을 받는거다.
# 따라서 구분이 없는 데이터를 입력받으려면 아래와 같이 사용하자.
# mapArray = []
# for i in range(0,N):
#     mapArray.append(list(map(int, input())))

input = sys.stdin.readline

N = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
isVisited = [[False] * (N) for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int,input().strip())))

def bfs(graph, nodeX,nodeY, isVisited):
    global houseCount
    q = deque()
    q.append((nodeX,nodeY))
    isVisited[nodeY][nodeX] = True

    while q:
        nodeX, nodeY = q.popleft()

        for i in range(4):
            nextX, nextY = nodeX + dx[i] , nodeY + dy[i]
            if nextX >= 0 and nextX < N and nextY >= 0 and nextY < N:
                if isVisited[nextY][nextX] == False and graph[nextY][nextX] == 1:
                    # print("nx ny : %d %d" %(nextX,nextY))
                    houseCount += 1
                    isVisited[nextY][nextX] = True
                    q.append((nextX,nextY))


groupCount = 0
house = []
for y in range(N):
    for x in range(N):
        if isVisited[y][x] == False and graph[y][x] == 1:
            houseCount = 1
            # print("y , x : %d %d" %(y,x))
            bfs(graph, x,y, isVisited)
            groupCount += 1
            house.append(houseCount)

house = sorted(house)
print(groupCount)
for i in house:
    print(i)

