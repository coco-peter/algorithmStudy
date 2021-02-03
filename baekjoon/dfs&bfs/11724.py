import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]
isVisited = [False] * (N+1)

for _ in range(M):
    startNode, endNode = map(int,input().split())
    graph[startNode].append(endNode)
    graph[endNode].append(startNode)

def dfs(graph, startNode, isVisited):

    isVisited[startNode] = True
    print(startNode)
    for i in graph[startNode]:
        if isVisited[i] == False:
            dfs(graph,i,isVisited)

# bfs만 되네...??
def bfs(graph, startNode, isVisited):
    q = deque()
    q.append(startNode)
    isVisited[startNode] = True

    while q:
        node = q.popleft()
        print(node)
        for i in graph[node]:
            if isVisited[i] == False:
                isVisited[i] = True
                q.append(i)

cost = 0
for i in range(1,N+1):

    if isVisited[i] == False:
        cost += 1
        bfs(graph,i,isVisited)

print("cost: %d" %cost)