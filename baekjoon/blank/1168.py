from collections import deque
import sys

N , M = map(int,sys.stdin.readline().split())
q = deque([i for i in range(1, N+1)])

res = []

while q:
    q.rotate(-M + 1)
    res.append(str(q.popleft()))

sys.stdout.write("<"+", ".join(res)+">")


