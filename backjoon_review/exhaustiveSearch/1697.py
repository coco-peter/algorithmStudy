import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int,input().split())

isVisited = [False] * 100001


def bfs(start):
    q = deque()
    q.append((start, 0))
    isVisited[start] = True

    while q:
        now, cnt = q.popleft()
        if now == K:
            break

        nowSub = now - 1
        nowAdd = now + 1
        nowMul = now * 2

        cnt += 1
        if nowAdd <= 100000 and isVisited[nowAdd] == False:
            q.append((nowAdd, cnt ))
            isVisited[nowAdd] = True
        if nowSub >= 0 and isVisited[nowSub] == False:
            q.append((nowSub, cnt))
            isVisited[nowSub] = True
        if nowMul <= 100000 and isVisited[nowMul] == False:
            q.append((nowMul, cnt))
            isVisited[nowMul] = True

    return cnt

print(bfs(N))