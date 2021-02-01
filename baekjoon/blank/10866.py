# 5m

from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
q = deque()
for _ in range(N):


    command = list(input().split())
    if command[0] == "push_back":
        q.append(int(command[1]))
    elif command[0] == "push_front":
        q.appendleft(command[1])
    elif command[0] == "front":
        if len(q)== 0:
            print("-1")
            continue
        print(q[0])
    elif command[0] == "back":
        if len(q)== 0:
            print("-1")
            continue
        print(q[len(q)-1])
    elif command[0] == "pop_front":
        if len(q)== 0:
            print("-1")
            continue
        print(q.popleft())
    elif command[0] == "pop_back":
        if len(q)== 0:
            print("-1")
            continue
        print(q.pop())
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        if len(q) == 0:
            print("1")
        else:
            print("0")

