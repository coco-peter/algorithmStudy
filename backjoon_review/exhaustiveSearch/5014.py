import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int,input().split())
isVisited = [False] * 1000001

def bfs(start):
    q = deque()
    q.append((start, 0))
    isVisited[False] = True

    while q:
        floor, cnt = q.popleft()

        if floor == G:
            return cnt
        # print(floor)
        cnt += 1
        tempFloor = floor + U
        if tempFloor <= F and isVisited[tempFloor] == False:
            q.append((tempFloor, cnt))
            isVisited[tempFloor] = True

        tempFloor = floor - D
        if tempFloor > 0 and isVisited[tempFloor] == False:
            q.append((tempFloor, cnt))
            isVisited[tempFloor] = True

    return -1





if S > G and D == 0:
    print("use the stairs")
elif S < G and U == 0:
    print("use the stairs")
else:
    res = bfs(S)
    if res == -1:
        print("use the stairs")
    else:
        print(res)