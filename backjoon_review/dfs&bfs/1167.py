import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    inputList = list(map(int,input().split()))

    for i in range(1, len(inputList)-1, 2):
        graph[inputList[0]].append((inputList[i], inputList[i+1]))

def bfs(startNode):
    global maxValue, maxNode
    q = deque()
    q.append((startNode, 0))
    isVisited[startNode] = True
    while q:
        node, cost = q.popleft()

        for i in graph[node]:
            if isVisited[i[0]] == False:
                isVisited[i[0]] = True
                q.append((i[0], i[1] + cost))
                if maxValue < i[1] + cost:
                    maxValue = i[1] + cost
                    maxNode = i[0]

maxValue = 0
maxNode = 0
isVisited = [False] * (N + 1)
bfs(1)

maxValue = 0
isVisited = [False] * (N + 1)
bfs(maxNode)
print(maxValue)