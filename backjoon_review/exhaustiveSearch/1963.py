import sys
from collections import deque

input = sys.stdin.readline

primeList = [False] * 10001

for i in range(2,5001):
    for j in range(i+i, 10001, i):
        if primeList[j] == False:
            primeList[j] = True


def bfs(start):
    q = deque()
    q.append((start,0))
    isVisited[start] = True

    while q:
        num, cnt = q.popleft()
        if num == endNum:
            return cnt

        strNum = str(num)

        cnt +=1
        for i in range(4):
            for j in map(str,range(10)):
                if i == 0 and j == "0":
                    continue

                nextNum = int(strNum[:i] + j + strNum[i+1:])
                if primeList[nextNum] == False and isVisited[nextNum] == False:
                    q.append((nextNum, cnt))
                    isVisited[nextNum] = True

for t in range(int(input())):
    startNum, endNum = map(int,input().split())
    isVisited = [False] * 10001
    print(bfs(startNum))