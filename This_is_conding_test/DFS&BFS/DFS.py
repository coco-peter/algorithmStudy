# DFS 정의
# 깊이 우선 탐색
# 깊은 부분을 우선적으로 탐색한다 -> 무슨뜻?
# 1. 시작 노드를 방문한다.
# 2. 방문한 노드는 스텍에 담는다.
# 3. 방문한 노드에서 가장 인접한( 보통 숫자가 낮은 노드를 ) 노드 중 방문하지 않은 노드를 방문하고 스텍에 담는다.
# 4. 만약 더이상 방문할 노드가 없다면 스텍에서 최상단 노드를 제거 후 3번으로
# 5. 더이상 방문할 노드가 없을때까지 반복한다.
# 6. DFS는 스텍의 구조를 띄고 있기때문에 재귀형태로 표현한다.

# DFS 구조 예시 code

def dfs(graph, startNode, isVisited):
    isVisited[startNode] = True                        #2 방문한 노드는 스텍에 담는다.
    print("%d " %startNode, end='')

    for i in graph[startNode]:                      #3  인접한 노드 중 가장 작은 것부터
        if isVisited[i] == False:                       #3  방문하지 않았다면
            dfs(graph, i,isVisited)                 #1,3  그 노드로 방문한다.

# 여기서 4번항목이 없는것처럼 보이지만 이는 재귀함수가 대채하고 있다. return이 따로 없는 이유도 이와 같다.
# 어차피 return을 따로 지정해주지 않아도 코드가 이상이 없다면 끝나게 되있기 때문이다. 만약 recursive 에러가 나면 코드가 잘못된거다...

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

dfs(graph, 1, isVisited)
# print(isVisited)
