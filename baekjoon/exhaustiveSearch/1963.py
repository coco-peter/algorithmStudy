import sys
from collections import deque
input = sys.stdin.readline

primeNumList = [0] * 10001

for i in range(2, 5000):
    if primeNumList[i] == False:
        start = i
        while start + i < len(primeNumList):
            start += i
            primeNumList[start] = True

def bfs():
    q = deque([(startNum, 0)])
    while q:
        num, value = q.popleft()

        if num == endNum:
            return value

        strNum = str(num)

        value += 1
        for i in range(4):
            for j in map(str,range(10)):
                if i == 0 and j == '0':
                    continue
                nextNum = int(strNum[:i] + j + strNum[i+1:])
                if primeNumList[nextNum] == False and isVisited[nextNum] == False:
                    isVisited[nextNum] = True
                    q.append((nextNum, value))



t = int(input())

for _ in range(t):
    startNum, endNum = map(int,input().split())
    isVisited = [False] * 10001
    print(bfs())