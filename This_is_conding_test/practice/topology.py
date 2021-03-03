# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4

# 1 2 5 3 6 4 7

from collections import deque

N, M = map(int, input().split())

indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    startNode, endNode = map(int,input().split())
    graph[startNode].append(endNode)
    indegree[endNode] += 1

def topologySort():
    q = deque()
    result = []

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        result.append(node)

        for i in graph[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    print(result, end = " ")

topologySort()