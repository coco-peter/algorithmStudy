import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append((start, ""))
    isVisited[start] = True

    while q:
        num, command = q.popleft()

        if num == endNum:
            return command

        print("num : %d" %num)
        nextNum = num * 2
        if nextNum > 9999:
            nextNum = nextNum % 10000

        print(nextNum)
        if isVisited[nextNum] == False:
            q.append((nextNum, command + "D"))
            isVisited[nextNum] = True



        #S
        nextNum = num -1
        if nextNum == -1:
            nextNum = 9999

        print(nextNum)
        if isVisited[nextNum] == False:
            q.append((nextNum, command + "S"))
            isVisited[nextNum] = True


        #L
        nextNum = int((num % 1000) * 10 + num / 1000)
        print(nextNum)
        if isVisited[nextNum] == False:
            q.append((nextNum, command + "L"))
            isVisited[nextNum] = True

        #R
        nextNum = int((num % 10) * 1000 + num / 10)
        if isVisited[nextNum] == False:
            q.append((nextNum, command + "R"))
            isVisited[nextNum] = True

        print(nextNum)

for t in range(int(input())):
    startNum , endNum = map(int,input().split())
    isVisited = [False] * 10001
    print(bfs(startNum))