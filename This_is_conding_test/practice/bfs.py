
# 1 2 3 8 7 4 5 6




graph = [[],
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]]


isVisited = [False] * 9


bfs(graph, 1, isVisited)
