
# 다익스트라는 최단경로 문제를 구할때 사용되는 알고리즘으로 가장 비용이 적은 노드를 선택하고 과정을 반복하는 알고리즘이다
# 기본 로직은 다음과 같다.
# 1. 출발 노드 선정
# 2. 최단 거리 테이블 초기화
# 3. 방문하지 않은 노드 중 가장 짧은 노드 선택
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용 계산 -> 최단 거리 테이블 갱신
# 5. 3, 4번 반복

# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2

# 데이터가(노드)가 10000개 이상이라면 input().split()로 문제 해결이 어려우므로 sys.stdin.readline을 사용하자.

import sys
input = sys.stdin.readline              # 이러면 input은 sys.stdin.readline의 기능을 수행한다. 그럼 input의 기존 기능은 무시??
INF = int(1e9)                          # 무한을 의미하는 10억

n, m = map(int, input().split())        # n 노드 , m 간선
start = int(input())

graph = [[] for i in range(n+1)]        # 노드와 간선의 정보를 저장하는 graph
distance = [INF] * (n+1)                # 출발 노드 기준 각 노드별 최단거리 --> 무한대로 초기화
isVisited = [0] * (n+1)

# 노드와 간선 데이터 입력 및 초기화
for i in range(m):
    startNode, endNode, value = map(int, input().split())
    graph[startNode].append((endNode,value))

def checkShortestNode():
    minValue = int(1e9)
    minIndex = 0
    for i in range(1,n+1):
        if distance[i] < minValue and isVisited[i] != 1:
            minValue = distance[i]
            minIndex = i


    return minIndex

def Dijkstra(startNode):
    distance[startNode]  = 0                # 자기 자신에 대한 거리는 0으로 처리
    isVisited[startNode] = True             # 방문했다.

    for j in graph[startNode]:              # 첫 노드에 연결되있는 노드 중에서
        distance[j[0]] = j[1]               # distance 초기화 얘는 굳이 INF와 비교 하지 않아도 됨. 어차피 연결되 있는녀석들은 INF보다 작을 거니까

    for i in range(n-1):
        shortestNode = checkShortestNode()          # 방문하지 않은 노드중 가장 짧은 노드 리턴
        isVisited[shortestNode] = 1                 # 가장 짧은 노드 방문 처리

        for k in graph[shortestNode]:               # 연결된 노드 중에서

            distanceOfNode = distance[shortestNode] + k[1]    # 자기 자신노드의 길이와 연결된 distance를 합친값이

            if distance[k[0]] > distanceOfNode:               # 기존에 초기화된 distance값보다 작은것이 있다면
                distance[k[0]] = distanceOfNode               # 초기화


Dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("Can't reach")
    else:
        print(distance[i])




