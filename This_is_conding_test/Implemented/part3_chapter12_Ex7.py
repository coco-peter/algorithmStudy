

# https://www.acmicpc.net/problem/15686
# python에서는 N개의 조합을 뽑아주는 combination 라이브러리가 있다... !!
# 컨셉을 생각 못한건 아닌데 이런게 있는지 몰랐음...
# 대부분 combination 방식으로 푼거 같다. 브루트 포스 방식으로 풀었다는데 이건 뭔지 나중에 다시 알아보자

from itertools import combinations


N , M = map(int, input().split())

chickenInfor = []
houseInfor = []

for y in range(N):
    a = list(map(int, input().split()))
    for x in range(N):
        if a[x] == 1:    # 집인경우
            houseInfor.append((y,x))
        elif a[x] == 2:   # 치킨집인경우
            chickenInfor.append((y,x))


candidates = list(combinations(chickenInfor, M))

# print(candidates)
# print(candidates[0][1][0])

def calculateDistance(candidate):
    minValue = int(1e9)
    totalDistance = 0
    for house in houseInfor:
        distance = minValue
        for i in range(M):
            y1, x1, y2, x2 = house[0] + 1, house[1] + 1, candidate[i][0] + 1 , candidate[i][1] + 1
            distance = min(distance, abs(y1-y2) + abs(x1-x2))
        totalDistance += distance


    return totalDistance

minDistance = int(1e9)
for candidate in candidates:

    eachDistance = calculateDistance(candidate)
    minDistance = min(minDistance, eachDistance)

print(minDistance)