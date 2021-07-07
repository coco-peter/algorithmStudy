import sys
sys.setrecursionlimit(100001)
input = sys.stdin.readline


def dfs(node):
    global result
    isVisited[node] = True
    nextNode = numList[node]
    groupMember.append(node)

    if isVisited[nextNode] == False:
        return dfs(nextNode)
    else:
        if nextNode in groupMember:
            result += groupMember[groupMember.index(nextNode):]
        return


for t in range(int(input())):
    N = int(input())
    numList = [0] + list(map(int,input().split()))
    # graph = [ [] * (N+1) for _ in range(N+1)]
    # for i in range(1, N + 1):
    #     graph[i].append(numList[i])
    #
    # print(graph)
    isVisited = [False] * (N + 1)
    result = []

    for i in range(1, N + 1):
        groupMember = []
        if isVisited[i] == False:
            dfs(i)

    print(N - len(result))