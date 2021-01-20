# 4
# 3
# 4
# 1
# 1

# 4
# 6
# 2
# 2
# 3
# 3
# 4
# 4



g = int(input())
p = int(input())

parentNode = [0] * (g+1)

for i in range(1,g+1):
    parentNode[i] = i

def findParnet(parentNode, node):
    if parentNode[node] != node:
        parentNode[node] = findParnet(parentNode,parentNode[node])

    return parentNode[node]

def unionNode(parentNode, startNode, endNode):
    startNodeParent = findParnet(parentNode,startNode)
    endNodeParent = findParnet(parentNode,endNode)

    if startNodeParent < endNodeParent:
        parentNode[endNodeParent] = startNodeParent
    else:
        parentNode[startNodeParent] = endNodeParent

count = 0
for _ in range(p):
    gatePosition = findParnet(parentNode,int(input()))
    if gatePosition == 0:
        break
    unionNode(parentNode,gatePosition, gatePosition-1)
    count += 1

print(count)

