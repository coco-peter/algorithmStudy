# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25

# 159

# 03/25 크루스칼 복습
import sys

input = sys.stdin.readline

N, M = map(int,input().split())
graph = []
parentNode = [0] * (N+1)

def findParent(parentNode, node):
    if parentNode[node] != node:
        parentNode[node] = findParent(parentNode, parentNode[node])

    return parentNode[node]

def unionNode(parentNode, firstNode, secondNode):
    firstNodeParent = findParent(parentNode, firstNode)
    secondNodeParent = findParent(parentNode, secondNode)

    if firstNodeParent < secondNodeParent:
        parentNode[secondNodeParent] = firstNodeParent
    else:
        parentNode[firstNodeParent] = secondNodeParent

for i in range(1, N+1):
    parentNode[i] = i

for _ in range(M):
    startNode, endNode, value = map(int,input().split())
    graph.append((value, startNode, endNode))

graph = sorted(graph)
minValue = 0
for i in graph:
    if findParent(parentNode, i[1]) != findParent(parentNode, i[2]):
        unionNode(parentNode, i[1], i[2])
        minValue+= i[0]

print(minValue)