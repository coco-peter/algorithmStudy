# 3 3
# 1 2
# 2 3
# 1 3


nodeCount, lineCount = map(int, input().split())

parentList = [0] * (nodeCount + 1)

def findParent(parentList, node):
    if parentList[node] != node:
        parentList[node] = findParent(parentList,parentList[node])

    return parentList[node]

def unionParent(parentList, firstNode, secondNode):

    firstNodeParent = findParent(parentList, firstNode)
    secondNodeParent = findParent(parentList, secondNode)

    if firstNodeParent > secondNodeParent:
        parentList[firstNodeParent] = secondNodeParent
    else:
        parentList[secondNodeParent] = firstNodeParent


for i in range(1, nodeCount+1):
    parentList[i] = i

isCycle = False


for i in range(lineCount):
    firstNode, secondNode = map(int, input().split())

    if findParent(parentList, firstNode) == findParent(parentList, secondNode):
        isCycle = True
    else:
        unionParent(parentList, firstNode,secondNode)

if isCycle == False:
    print("사이클이 발생하지 않았습니다")
else:
    print("사이클이 발생했습니다.")


# for i in range(1,nodeCount+1):
#     print("%d " %parentList[i], end="")
#
# print("")
# for i in range(1,nodeCount+1):
#     findRootNode = findParent(parentList,i)
#     print("%d " %findRootNode, end="")

