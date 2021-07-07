# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3



import sys

N, M = map(int, input().split())
parentNode = [0] * (N+1)

for i in range(1,N+1):
    parentNode[i] = i

def checkParent(parentNode, node):
    if parentNode[node] != node:
        parentNode[node] = checkParent(parentNode,parentNode[node])

    return parentNode[node]

def unionNode(parentNode,startNode, endNode):
    startNodeParent = checkParent(parentNode,startNode)
    endNodeParent = checkParent(parentNode,endNode)

    if startNodeParent < endNodeParent:
        parentNode[endNodeParent] = startNodeParent
    else:
        parentNode[startNodeParent]= endNodeParent

for y in range(N):
    mapList = list(map(int, input().split()))
    for x in range(N):
        if mapList[x] == 1:
            unionNode(parentNode, y+1,x+1)

checkList = list(map(int, input().split()))

isPossible = True
for i in range(0,M-2):
    if checkParent(parentNode,checkList[i]) != checkParent(parentNode,checkList[i+1]):
        isPossible = False

print(parentNode)
if isPossible:
    print("YES")
else:
    print("NO")
