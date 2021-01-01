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

# 3 2 1
# 1 2 4
# 1 3 2

# 데이터가(노드)가 10000개 이상이라면 input().split()로 문제 해결이 어려우므로 sys.stdin.readline을 사용하자.

import sys
import heapq
input = sys.stdin.readline              # 이러면 input은 sys.stdin.readline의 기능을 수행한다. 그럼 input의 기존 기능은 무시??
INF = int(1e9)                          # 무한을 의미하는 10억

N, M, C = map(int, input().split())

graph = [[] for i in range(N+1)]        # 노드와 간선 정보 저장.
distance = [INF] * (N+1)

for i in range(M):
    startNode, endNode, value = map(int, input().split())
    graph[startNode].append((value,endNode))

def Dijkstart(startNode):
    q = []
    heapq.heappush(q,(0,startNode))
    distance[startNode] = 0

    while q:
        value, nowNode = heapq.heappop(q)

        if distance[nowNode] < value:
            continue

        for i in graph[nowNode]:
            cost = value + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q,(cost,i[1]))

Dijkstart(C)
count = 0
maxValue = 0
for i in range(1,N+1):
    if distance[i] != INF and distance[i] != 0:
        count += 1
        if maxValue < distance[i]:
            maxValue = distance[i]

print(distance)
print(count, maxValue)








