# 신장 트리란 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
# 크루스칼 알고리즘이란 최소한의 비용으로 신장 트리를 찾는 알고리즘 = 최소신장트리 알고리즘
# 크루스칼 알고리즘은 최소비용을 찾는다는 점에서 그리디 알고리즘으로 분류됨.

# [로직]
# 1. 간선 데이터를 비용에 따라 오름차순 정렬
# 2. 간선을 확인하면서 사이클 발생 여부 체크
#   2-1. 사이클이 발생하지 않는경우 최소 신장 트리에 포함
#   2-2. 사이클이 발생하는 경우 최소 신장 트리 포함 X
# 3. 모든 간선에 대해 2번 과정 반복.

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

nodeCount, lineCount = map(int, input().split())
INF = int(1e9)

lineValueList = []
parentList = [0] * (nodeCount+1)

def findParent(parentList, node):
    if parentList[node] != node:
        parentList[node] = findParent(parentList, parentList[node])

    return parentList[node]

def unionNode(parentList, firstNode, secondNode):

    firstNodeParent  = findParent(parentList, firstNode)
    secondNodeParent = findParent(parentList, secondNode)

    if firstNodeParent < secondNodeParent:
        parentList[secondNodeParent] = firstNodeParent
    else:
        parentList[firstNodeParent] = secondNodeParent


for i in range(1,nodeCount+1):
    parentList[i] = i

for i in range(lineCount):
    firstNode, secondNode, lineValue = map(int, input().split())
    lineValueList.append((lineValue,firstNode,secondNode))

lineValueList = sorted(lineValueList)

minValue = 0
for value in lineValueList:

    if parentList[value[1]] != parentList[value[2]]:
        unionNode(parentList,value[1],value[2])
        minValue += value[0]

print(parentList)
print(minValue)



