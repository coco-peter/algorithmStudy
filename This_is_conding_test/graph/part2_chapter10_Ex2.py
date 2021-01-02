# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4

# 최소비용으로 신장트리를 구성하는것은 크루스칼 알고리즘이다 !! 위상정렬이 아니고...
# 추가로 두개의 마을을 만드는게 맞음 ㅡㅡ 즉 최소비용으로 만들어야하니까 최대 배용 간선을 제거해 버리면 되는거다
# 아 참고로 위상정렬은 순서가 정해져있는 리스트의 작업을 수행해야할때 사용하는 알고리즘.

N, M = map(int, input().split())

graph = []
nodeParent = [0] * (N+1)
for i in range(M):
    firstNode, secondNode, value = map(int, input().split())
    graph.append((value,firstNode,secondNode))

def findParent(nodeParent, node):
    if nodeParent[node] != node:
        nodeParent[node] = findParent(nodeParent,nodeParent[node])

    return nodeParent[node]

def unionParent(nodeParent, firstNode, secondNode):

    firstNodeParent = findParent(nodeParent,firstNode)
    secondNodeParent = findParent(nodeParent,secondNode)

    if firstNodeParent < secondNodeParent:
        nodeParent[secondNodeParent] = firstNodeParent
    else:
        nodeParent[firstNodeParent] = secondNodeParent


for i in range(1, N+1):
    nodeParent[i] = i

graph = sorted(graph)

result = 0
last = 0
for i in graph:
    if findParent(nodeParent,i[1]) != findParent(nodeParent,i[2]):
        unionParent(nodeParent,i[1],i[2])
        result += i[0]
        last = i[0]

print(result-last)



