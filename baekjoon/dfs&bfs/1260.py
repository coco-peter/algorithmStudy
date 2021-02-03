import sys
from collections import deque
input = sys.stdin.readline

N, M , V = map(int,input().split())

graph = [[] for _ in range(N+1)]
isVisited = [0] * (N+1)
for _ in range(M):
    startNode, endNode = map(int,input().split())
    graph[startNode].append(endNode)
    graph[endNode].append(startNode)
    graph[startNode] = sorted(graph[startNode])
    graph[endNode] = sorted(graph[endNode])


def dfs(graph, startNode, isVisited):
    print("%d " %startNode, end="")
    isVisited[startNode] = True

    for i in graph[startNode]:
        if isVisited[i] == False:
            isVisited[i] = True
            dfs(graph,i,isVisited)

def bfs(graph, startNode, isVisited):

    q = deque()
    q.append(startNode)
    isVisited[startNode] = True
    while q:
        node = q.popleft()
        print("%d "%node, end="")

        for k in graph[node]:
            if isVisited[k] == False:
                isVisited[k] = True
                q.append(k)


dfs(graph,V,isVisited)
print("")
isVisited = [0] * (N+1)
bfs(graph,V,isVisited)

