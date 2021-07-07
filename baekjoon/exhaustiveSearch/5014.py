import sys
from collections import deque
import copy

input = sys.stdin.readline

F, S, G, U, D = map(int,input().split())

isVisited = [0] * (F+1)

def bfs(start):
    q = deque([(start, 0)])
    visited = {start}
    while q:
        curFloor, cnt = q.popleft()

        # print(isVisited)
        # print(curFloor)
        # print(cnt)
        if curFloor == G:
            return cnt

        cnt += 1
        if curFloor + U <= F and curFloor + U not in visited:
            q.append((curFloor + U, cnt))
            visited.add(curFloor + U)
        if curFloor - D >= 1 and curFloor - D not in visited:
            q.append((curFloor - D, cnt))
            visited.add(curFloor - D)

    return "use the stairs"
#
# if U == D == 0:
#     print("use the stairs")
# elif S == G:
#     print(0)
# elif S < G and D == 0:
#     if (G - S) % U == 0:
#         print((G - S) // U)
#     else:
#         print("use the stairs")
# elif S < G and U == 0:
#     print("use the stairs")
# elif S > G and U == 0:
#     if (S - G) % D == 0:
#         print((S - G) // D)
#     else:
#         print("use the stairs")
# elif S > G and D == 0:
#     print("use the stairs")
# elif U == D:
#     if S < G:
#         if (G - S) % U == 0:
#             print((G - S) // U)
#         else:
#             print("use the stairs")
#     elif S > G:
#         if (S - G) % D == 0:
#             print((S - G) // D)
#         else:
#             print("use the stairs")
# else:
print(bfs(S))