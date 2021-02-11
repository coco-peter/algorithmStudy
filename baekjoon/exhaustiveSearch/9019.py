import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    ans = ""
    q = deque([(startNum, ans)])
    isVisited[startNum] = True

    while q:
        num, res = q.popleft()
        num = int(num)
        # print(num , res)
        if num == targetNum:

            return res

        temp = num - 1
        if temp == -1:
            temp = 9999
        if isVisited[temp] == False:
            isVisited[temp] = True
            tempRes = res + "S"
            q.append((temp, tempRes))

        temp = num * 2
        if temp > 9999:
            temp = temp % 10000
        if isVisited[temp] == False:
            isVisited[temp] = True
            tempRes = res + "D"
            q.append((temp, tempRes))

        temp = int((num % 10) * 1000 + num / 10)

        # print("R: %s %d" %(temp, num))
        if isVisited[int(temp)] == False:
            isVisited[int(temp)] = True
            tempRes = res + "R"
            q.append((temp, tempRes))

        # for문해도 시간 얼마 안걸리거라고 생각했는데...
        temp = int((num % 1000) * 10 + num / 1000)

        # print("L: %s %d" %(temp, num))
        if isVisited[int(temp)] == False:
            isVisited[int(temp)] = True
            tempRes = res + "L"
            q.append((temp, tempRes))






for _ in range(int(input())):
    startNum, targetNum = map(int, input().split())
    isVisited = [0] * 10001
    print(bfs())

