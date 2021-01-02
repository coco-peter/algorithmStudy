# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

from collections import deque
import copy
INF = int(1e9)
N = int(input())

graph = [[] for i in range(N+1)]
edge = [0] * (N+1)
time = [0] * (N+1)
for i in range(1,N+1):
    dataList = list(map(int, input().split()))
    time[i] = dataList[0]
    for j in dataList[1:-1]:
        graph[j].append(i)
        edge[i] += 1

def topologySort():
    result = copy.deepcopy(time)                            # 그냥 대입 연산하면 같이 바껴버린다. 주소를 참조하기 때문에 따라서 값만 가져오는걸 사용한다.
    q = deque()
    for i in range(1,N+1):
        if edge[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        for i in graph[node]:
            edge[i] -= 1
            result[i] = max(result[i], result[node] + time[i])
            if edge[i] == 0:
                q.append(i)

    for i in range(1,N+1):
        print("%d " %result[i], end="")

topologySort()
