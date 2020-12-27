# BFS 정의
# 너비 우선 탐색
# 가까운 부분을 우선적으로 탐색한다 -> 무슨뜻?
# 1. 시작 노드를 큐에 삽입하고 방문한다.
# 2. 큐에서 노드를 꺼내서 해당 노드에 인접한 노드 (보통 숫자가 낮은 노드를)중에 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
# 3. 큐가 빌때까지 2번을 반복

# BFS 구조 예시 code

from collections import deque

def bfs(graph, startNode, isVisited):

    queue = deque([startNode])                      # deque가 queue에 담는 기능
    isVisited[startNode] = True                     # 방문처리
    # print("%d " %startNode, end="")
    print(queue)                                    # 이건 배열이여 뭐여
    print(queue[0])
    while queue:                                    # 큐가 비었는지를 이렇게 확인하는것 같다. 큐가 있으면 반복한다는 뜻
        popNode = queue.popleft()
        print("%d " %popNode, end="")
        for i in graph[popNode]:
            if isVisited[i] == False:
                queue.append(i)
                isVisited[i] = True




# 0번 노드는 없으므로 빈칸, 1번 노드부터 숫자가 작은 순으로 입력
graph = [[],
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]]

# 0이 담긴 9 크기의 배열을 다음과 같이 선언할 수 있다. Tip
isVisited = [False] * 9
# print(isVisited)

bfs(graph, 1, isVisited)

