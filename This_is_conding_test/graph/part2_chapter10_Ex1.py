# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1

# 그냥 find랑 union구현 가능하냐 물보는 문제.

N, M = map(int, input().split())

nodeParent = [0] * (N+1)

for i in range(N+1):
    nodeParent[i] = i

def findParent(nodeParent, node):
    if nodeParent[node] != node:
        nodeParent[node] = findParent(nodeParent,nodeParent[node])

    return nodeParent[node]

def unionNode(nodeParent, firstNode, secondNode):

    firstNodeParent = findParent(nodeParent,firstNode)
    secondNodeParent = findParent(nodeParent,secondNode)

    if firstNodeParent < secondNodeParent:
        nodeParent[secondNodeParent] = firstNodeParent
    else:
        nodeParent[firstNodeParent] = secondNodeParent


for i in range(M):
    command, firstNode, secondNode = map(int, input().split())

    if command == 0:
        unionNode(nodeParent,firstNode,secondNode)
    else:
        firstNodeParent = findParent(nodeParent, firstNode)
        secondNodeParent = findParent(nodeParent, secondNode)

        if firstNodeParent == secondNodeParent:
            print("YES")
        else:
            print("NO")