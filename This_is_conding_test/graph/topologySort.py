# 위상정렬은 정렬 알고리즘의 일종
# 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘
# 방향 그래프의 모든 노드를 "방향성에 거스르지 않도록 순서대로 나열하는 것"

# [로직]
# 1. 진입차수가 0인 노드를 큐에 넣는다
# 2. 큐가 빌 때까지 다음의 과정을 반복한다.
#   2-1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
#   2-2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.

# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4

# 03/28 위상정렬 복습
from collections import deque

nodeCount, lineCount = map(int, input().split())

indegree = [0] * (nodeCount+1)
graph = [[] for _ in range(nodeCount+1)]

for i in range(lineCount):
    startNode, endNode = map(int, input().split())
    graph[startNode].append(endNode)
    indegree[endNode] += 1


def topoloySort():
    q = deque()
    result = []

    for i in range(1, nodeCount+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        nowNode = q.popleft()
        result.append(nowNode)
        for i in graph[nowNode]:

            if indegree[i] > 0:                     # 사실 0인것만 넣는것이기 때문에 굳이 이 조건문을 넣지 않아도 상관은 없다.
                indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print("%d " %i, end="")

topoloySort()






