import sys

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
isVisited = [False] * (N+1)

def dfs(node,cost):
    isVisited[node] = True
    for k in graph[node]:
        if isVisited[k[0]] == False:
            dfs(k[0],cost + k[1])
    # print(node, cost)
    costList.append(cost)


for _ in range(N):
    inputList = list(map(int,input().split()))
    for k in range(1,len(inputList)-1, 2):    # 와 아직 멀었다 멀었어...
        graph[inputList[0]].append((inputList[k], inputList[k+1]))

# print(graph)

res = 0


cost = 0
costList = []
dfs(1,cost)
isVisited = [False] * (N + 1)
# print(costList)
res = max(max(costList), res)

print(res)