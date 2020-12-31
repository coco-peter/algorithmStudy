# 기존 다익스트라 코드는 시간 복잡도가 O(V^2)이다 V는 노드의 갯수
# 즉 시간 복잡도를 줄이기 위해서 개선된 다익스트라 코드를 설계해야하며 이는 우선순위 큐를 이용하여 해결할 수 있다.
# 우선순위 큐는 힙을 이용하는데 가장 값이 낮은 데이터를 출력한다.
# 즉 기존 코드에서 checkshortestNode 함수를 구현할 필요가 없어진다.
# 로직은 다음과 같다.
# 1. 출발 노드 선정
# 2. 출발 노드 (0,1)을 우선순위 큐에 삽입 --> (간선, 노드) 자기자신은 0임을 확인 파이썬의 heapq라이브러리는 튜플을 원소로 받으면 첫번째 원소를 기준으로 우선순위 큐를 선정한다.
# 3. 가장 짧은 노드를 선택하기 위해서는 우선순위 큐에서 걍 꺼내면 됨. 꺼낸 노드는 방문처리
# 4. 그 노드에 연결된 노드중에 방문한적 있다면 걍 패스
# 5. 만약 방문한적 없다면 각 노드에 연결된 노드에 대한 최소 비용 계산
# 6. 계산된 노드들만 큐에 삽입.
# 7. 3-6 반복

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
import heapq
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

def Dijkstra(startNode):


    q = []
    heapq.heappush(q,(0,start))             # 시작 노드에 대한 (거리,노드) 설정
    distance[startNode]  = 0                # 자기 자신에 대한 거리는 0으로 처리
    # isVisited[startNode] = True           # 여기서는 방문했다는 의미를 별도에 리스트에 저장하지 않고 거리값이 작다면 이미 계산되있느것으로 간주한다.

    while q:                                # 큐가 빌때까지 반복

        dist, nowNode = heapq.heappop(q)    # q라는 배열에서 가장 짧은 노드를 꺼내자

        if distance[nowNode] < dist:        # 만약 꺼낸 노드의 간선값이 현재 dist값보다 작다면 이미 계산된것으로 간주.
            continue

        for k in graph[nowNode]:               # 연결된 노드 중에서

            distanceOfNode = dist + k[1]    # 자기 자신노드의 길이와 연결된 distance를 합친값이

            if distance[k[0]] > distanceOfNode:               # 기존에 초기화된 distance값보다 작은것이 있다면
                distance[k[0]] = distanceOfNode               # 초기화
                heapq.heappush(q, (distanceOfNode, k[0]))     # 초기화된 노드는 큐에 담는다.


Dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("Can't reach")
    else:
        print(distance[i])




