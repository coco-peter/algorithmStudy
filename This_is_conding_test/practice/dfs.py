
# 1 2 7 6 8 3 4 5




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


dfs(graph, 1, isVisited)

