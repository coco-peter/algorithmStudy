import sys
from collections import deque


input = sys.stdin.readline

bottleList = [0] * 11

candidateList = []
resList = []

def bfs(A,B,C,cnt):
    q = deque([(A,B,C,cnt)])
    candidateList.append((A,B,C))
    bottleList[8], bottleList[9], bottleList[10] = A, B, C

    while q:
        x,y,z,cnt = q.popleft()

        if x == 0:
            if z not in resList:
                resList.append(z)

        for i in range(8,11):
            if bottleList[i] == 0:
                continue

            if i == 10:
                A = 


bfs(0,0,10,0)