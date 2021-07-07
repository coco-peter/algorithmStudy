import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[] * (N + 1) for _ in range(N+1)]
isVisited = [False] * (N+1)
for _ in range(M):
    startNode, endNode = map(int,input().split())
    graph[startNode].append(endNode)
    graph[endNode].append(startNode)


def bfs(startNode):
    q = deque()
    q.append(startNode)
    isVisited[startNode] = True

    while q:
        nowNode = q.popleft()

        for i in graph[nowNode]:
            if isVisited[i] == False:
                isVisited[i] = True
                q.append(i)

cnt = 0
for i in range(1,N + 1):
    if isVisited[i] == False:
        bfs(i)
        cnt += 1

print(cnt)
