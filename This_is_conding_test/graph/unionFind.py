#
# 6 4
# 1 4
# 2 3
# 2 4
# 5 6



nodeCount, lineInformation = map(int, input().split())
parentList = [0] * (nodeCount+1)

def findParentNode(parentList, node):
    if parentList[node] != node:                                             # 부모노드 배열과 node가 같지 않은 경우에는
        parentList[node] = findParentNode(parentList, parentList[node])      # 같을때까지 재귀

    return parentList[node]                                                  # 같을때까지 재귀한 값이다.

def unionNode(parentList,firstNode,secondNode):

    firstNodeParent = findParentNode(parentList, firstNode)
    secondNodeParent = findParentNode(parentList, secondNode)
    print(firstNodeParent, secondNodeParent)
    if firstNodeParent > secondNodeParent:
        parentList[firstNodeParent] = secondNodeParent
    else:
        parentList[secondNodeParent] = firstNodeParent
    print(parentList)

for i in range(1, nodeCount+1):
    parentList[i] = i

for i in range(lineInformation):
    firstNode, secondNode = map(int, input().split())
    unionNode(parentList,firstNode,secondNode)

for i in range(1, nodeCount+1):
    print(parentList[i])

