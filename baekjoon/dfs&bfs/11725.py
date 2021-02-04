
from collections import deque
import sys

input = sys.stdin.readline


N = int(input())
graph = [[] * (N+1) for _ in range(N+1)]
parentNode = [0] * (N+1)
isVisited = [False] * (N+1)

for _ in range(N-1):
    startNode, endNode = map(int,input().split())
    graph[startNode].append(endNode)
    graph[endNode].append(startNode)

for i in range(1,N+1):
    parentNode[i] = i

def bfs(node):
    q = deque([node])
    isVisited[node] = True
    parentNode[node] = node
    while q:
        node = q.popleft()
        for k in graph[node]:
            if isVisited[k] == False:
                q.append(k)
                isVisited[k] = True
                parentNode[k] = node


bfs(1)
for i in parentNode[2:]:
    print(i)