# 7 11
# 0 1 7
# 0 3 5
# 1 2 8
# 1 3 9
# 1 4 7
# 2 4 5
# 3 4 15
# 3 5 6
# 4 5 8
# 4 6 9
# 5 6 11




import sys

input = sys.stdin.readline

N, M = map(int, input().split())

distance = []
parentNode = [0] * (N+1)

for _ in range(M):
    X, Y, Z = map(int, input().split())
    distance.append((Z,X,Y))

distance = sorted(distance)
print(distance)
for i in range(1,N+1):
    parentNode[i] = i

def findParent(parentNode, node):
    if parentNode[node] != node:
        parentNode[node] = findParent(parentNode,parentNode[node])

    return parentNode[node]

def unionNode(parentNode, startNode, endNode):
    startNodeParent = findParent(parentNode,startNode)
    endNodeParent = findParent(parentNode,endNode)

    if startNodeParent < endNodeParent:
        parentNode[endNodeParent]= startNodeParent
    else:
        parentNode[startNodeParent] = endNodeParent

cost = 0
total = 0
for k in distance:
    total += k[0]
    if findParent(parentNode,k[1]) != findParent(parentNode,k[2]):
        unionNode(parentNode, k[1],k[2])
        cost += k[0]
print(parentNode)
print(total-cost)


