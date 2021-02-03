import sys
sys.setrecursionlimit(100001)
input = sys.stdin.readline

def dfs(graph, startNode, isVisited):
    global result
    isVisited[startNode] = True
    nextNode = graph[startNode]
    groupMember.append(startNode)
    if isVisited[nextNode] == False:
        dfs(graph,nextNode,isVisited)
    else:
        if nextNode in groupMember:

            result += groupMember[groupMember.index(nextNode):]
        return

for _ in range(int(input())):
    N = int(input())
    graph = [0] + list(map(int,input().split()))
    isVisited = [0] * (N+1)
    result = []
    for i in range(1,N+1):
        groupMember = []
        if isVisited[i] == False:
            dfs(graph, i, isVisited)

    print(N - len(result))
