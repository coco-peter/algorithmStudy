import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

def bfs(graph, startNode, isVisited):
    q = deque()
    q.append(startNode)
    isVisited[startNode] = 1

    while q:
        node = q.popleft()
        for i in graph[node]:
            if isVisited[i] == 0:
                isVisited[i] = -isVisited[node]
                q.append(i)
            else:
                if isVisited[i] == isVisited[node]:
                    return False

    return True


for _ in range(T):
    N, M = map(int,input().split())
    graph = [ [] for _ in range(N+1)]
    isVisited = [0] * (N+1)

    for _ in range(M):
        startNode, endNode = map(int,input().split())
        graph[startNode].append(endNode)
        graph[endNode].append(startNode)

    result = True

    for i in range(1,N+1):
        if isVisited[i] == 0:
            if bfs(graph,i,isVisited) == False:
                result = False
                break

    if result:
        print("YES")
    else:
        print("NO")