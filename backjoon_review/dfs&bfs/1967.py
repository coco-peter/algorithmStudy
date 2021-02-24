import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] * (N+1) for _ in range(N+1)]

for _ in range(N-1):
    startNode, endNode, value = map(int,input().split())
    graph[startNode].append((endNode, value))
    graph[endNode].append((startNode, value))

def bfs(startNode):
    global maxValue, maxNode
    q = deque()
    q.append((startNode, 0))
    isVisited[startNode] = True
    while q:
        node, cost = q.popleft()

        for nextNode, nextCost in graph[node]:
            if isVisited[nextNode] == False:
                isVisited[nextNode] = True
                q.append((nextNode, cost + nextCost))
                if maxValue < cost + nextCost:
                    maxValue = cost + nextCost
                    maxNode = nextNode


maxValue, maxNode = 0, 0
isVisited = [0] * (N + 1)
bfs(1)


maxValue = 0
isVisited = [0] * (N + 1)
bfs(maxNode)

print(maxValue)

