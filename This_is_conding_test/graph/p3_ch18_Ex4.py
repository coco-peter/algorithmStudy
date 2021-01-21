# https://www.acmicpc.net/problem/2887

# 5
# 11 -15 -15
# 14 -5 -15
# -1 -1 -5
# 10 -4 -1
# 19 -4 19



import sys

input = sys.stdin.readline

N = int(input())
distance = []
nodeParent = [0] * N
eachPlanetInfor = [] * N
for i in range(N):
    nodeParent[i] = i
    x, y, z = map(int, input().split())
    eachPlanetInfor.append((x,y,z))


# print(eachPlanetInfor)
# i에서 j로 가는 비용 정리
for i in range(N):
    for j in range(i+1,N):
        cost = min(abs(eachPlanetInfor[i][0] - eachPlanetInfor[j][0]), abs(eachPlanetInfor[i][1] - eachPlanetInfor[j][1]), abs(eachPlanetInfor[i][2] - eachPlanetInfor[j][2]))
        distance.append((cost,i, j))

# print(distance)
distance = sorted(distance)

def findParent(nodeParent, node):
    if nodeParent[node] != node:
        nodeParent[node] = findParent(nodeParent, nodeParent[node])

    return nodeParent[node]

def unionParent(nodeParent, startNode, endNode):
    startNodeParent = findParent(nodeParent,startNode)
    endNodeParent = findParent(nodeParent,endNode)

    if startNodeParent < endNodeParent:
        nodeParent[endNodeParent] = startNodeParent
    else:
        nodeParent[startNodeParent] = endNodeParent

result = 0
for k in distance:
    if findParent(nodeParent,k[1]) != findParent(nodeParent,k[2]):
        unionParent(nodeParent,k[1],k[2])
        result += k[0]

# print(nodeParent)
print(result)