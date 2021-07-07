from collections import deque


N , M = map(int,input().split())
q = deque()

for i in range(1, N+1):
    q.append(i)

print("<", end="")
while q:
    if len(q) == 1:
        print(q.popleft(),end="")
        print(">", end="")
        break

    for i in range(M-1):
        q.append(q[0])
        q.popleft()

    print(q.popleft(), end="")
    print(", ", end="")

