import sys

input = sys.stdin.readline

def pairStudent(start, cnt):

    if cnt == 0:
        return 1

    pairCnt = 0
    for i in range(start, n):
        if isVisited[i] == False:
            for j in range(i + 1, n):
                if isVisited[j] == False and isPaired[i][j] == True:
                    isVisited[i] = isVisited[j] = True
                    pairCnt += pairStudent(i, cnt - 2)
                    isVisited[i] = isVisited[j] = False

    return pairCnt



for t in range(int(input())):
    n, m = map(int, input().split())


    isVisited = [False] * n
    isPaired = [[False] * n for _ in range(n)]
    noList = list(map(int,input().split()))

    for i in range(0, len(noList), 2):
        isPaired[noList[i]][noList[i+1]] = True
        isPaired[noList[i+1]][noList[i]] = True

    print(pairStudent(0, n))
