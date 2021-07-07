import sys
from collections import deque


input = sys.stdin.readline

T = int(input())

def bfs(graph, startNode, isVisited):
    q = deque()
    q.append(startNode)
    isVisited[startNode] = True

    while q:
        node = q.popleft()
        for i in graph[node]:
            if isVisited[i] == False:
                isVisited[i] = True
                q.append(i)



for _ in range(T):
    N = int(input())
    nodeList = list(map(int,input().split()))
    graph = [[] for _ in range(N+1)]
    isVisited = [False] * (N+1)
    for i in range(len(nodeList)):
        graph[i+1].append(nodeList[i])
        graph[nodeList[i]].append(i+1)

    count = 0
    for i in range(1,N+1):
        if isVisited[i] == False:
            count += 1
            bfs(graph,i,isVisited)

    print(count)
