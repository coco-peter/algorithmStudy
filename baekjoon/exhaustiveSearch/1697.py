import sys
from collections import deque


input = sys.stdin.readline

N, K = map(int,input().split())
isVisited = [0] * 100001
minValue = 100000

def searchK(start):
    cnt = 0
    q = deque([(start,cnt)])

    while q:
        node, value = q.popleft()
        if not isVisited[node]:
            isVisited[node] = True
            if node == K:
                return value
            value += 1
            if (node + 1) <= 100000:
                q.append((node + 1, value))
            if (node * 2) <= 100000:
                q.append((node * 2, value))
            if (node -1 ) >= 0:
                q.append((node - 1, value))
    return value
print(searchK(N))
