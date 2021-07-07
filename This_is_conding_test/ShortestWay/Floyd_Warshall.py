# 플로이드 와샬 알고리즘
# 다익스트라는 한 노드에서 다른노드로 가는 지점에 대해 가장 짧은 경로를 계산하는거라면
# 플로이드 와샬 알고리즘은 모든 노드에서 다른 모든 노드로가는 가장 짧은 경로를 계산하는것이다.
# 일단 시간 복잡도는 O(N^3)이다.
# 0부터 노드갯수까지 반복해야하며, 각 노드에서 연결된 다른 노드들과도 반복해야하며 , 또한 노드에서 노드를 거쳐가는 노드쌍과도 비교해야하기 때문.
# 우선 체크와 상관없이 계속 반복하면서 확인하면 된다.
# D(a,b) = min(D(a,b), D(a,k,b))

# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2

import sys

INF = int(1e9)
input = sys.stdin.readline
n = int(input())                                # node 개수
m = int(input())                                # 간선 정보

graph = [[INF] * (n+1) for i in range(n+1)]     # 책에서는 자꾸 2차배열을 이런식으로 사용하네..??

for x in range(1,n+1):
    for y in range(1,n+1):
        if y == x:
            graph[y][x] = 0

for i in range(m):
    startNode, endNode, value = map(int, input().split())
    graph[startNode][endNode] = value

for i in range(1, n+1):                     # i를 거쳐가는 노드 중에
    for j in range(1, n+1):                 # 근데 j가 i랑 같은 경우는 빼야하는거 아닌가?? 아 어차피 0이라서 0으로 남아있나?
        for k in range(1, n+1):             # j -> k로 가는 최소 비용 계산
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])       # j->k = min(j->k , j->i + i->k)

for y in range(1,n+1):
    for x in range(1,n+1):
        if graph[y][x] == INF:
            print("INF ", end="")
        else:
            print("%d "%graph[y][x], end="")
    print("")