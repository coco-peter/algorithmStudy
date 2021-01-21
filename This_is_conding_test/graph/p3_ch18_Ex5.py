# https://www.acmicpc.net/problem/3665

from collections import deque
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    lastYearList = list(map(int, input().split()))

    for i in range(n):
        for j in range(i+1, n):
            graph[lastYearList[i]][lastYearList[j]] = True
            indegree[lastYearList[j]] += 1

    for cc in range(int(input())):
        startNode, endNode = map(int,input().split())

        if graph[startNode][endNode]:
            graph[startNode][endNode] = False
            graph[endNode][startNode] = True
            indegree[endNode] -= 1
            indegree[startNode] += 1
        else:
            graph[startNode][endNode] = True
            graph[endNode][startNode] = False
            indegree[endNode] += 1
            indegree[startNode] -= 1

    result = []
    q = deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    isPossible = False
    isCertain = True

    for i in range(n):

        if len(q) == 0:
            isPossible = True
            break
        if len(q) >= 2:
            isCertain = False
            break

        nowNode = q.popleft()
        result.append(nowNode)

        for j in range(1, n+1):
            if graph[nowNode][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if isPossible:
        print("IMPOSSIBLE")
    elif not isCertain:
        print("?")
    else:
        for i in range(n):
            print("%d " %result[i], end="")
        print("")

