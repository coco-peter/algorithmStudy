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

x_list = []
y_list = []
z_list = []
for i in range(N):
    nodeParent[i] = i
    x, y, z = map(int, input().split())
    x_list.append((x,i))
    y_list.append((y,i))
    z_list.append((z,i))

x_list.sort()
y_list.sort()
z_list.sort()

for i in range(N-1):
    distance.append((x_list[i+1][0]-x_list[i][0], x_list[i][1], x_list[i+1][1]))
    distance.append((y_list[i + 1][0] - y_list[i][0], y_list[i][1], y_list[i + 1][1]))
    distance.append((z_list[i + 1][0] - z_list[i][0], z_list[i][1], z_list[i + 1][1]))


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