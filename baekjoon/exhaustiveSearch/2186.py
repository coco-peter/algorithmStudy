import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int,input().split())

# graph = [[0] * M for _ in range(N)]
graph = [list(input().rstrip()) for _ in range(N)]
targetWord = input().rstrip()
q = deque()

for y in range(N):
    for x in range(M):
        if graph[y][x] == targetWord[0]:
            res = graph[y][x]
            q.append((x,y,res,0))


# dx = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# dy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

def bfs():
    global cnt
    global K

    while q:
        x, y, word, pos = q.popleft()
        # print(word)
        if str(word) == targetWord:
            cnt += 1

        pos += 1
        for K in range(1,K+1):
            # if abs(dx[i]) <= K and abs(dy[i]) <= K:
            for a, b in [0,K],[K,0],[0,-K],[-K,0]:
                # nx , ny = x + dx[i] , y + dy[i]
                nx, ny = x + a, y + b
                if 0 <= nx < M and 0 <= ny < N and pos < len(targetWord) and targetWord[pos] == graph[ny][nx]:
                    q.append((nx, ny, word + graph[ny][nx], pos))


bfs()

print(cnt)