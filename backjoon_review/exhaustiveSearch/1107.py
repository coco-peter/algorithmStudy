import sys

input = sys.stdin.readline

N = input()

M = int(input())

brokenBtn = list(map(int,input().split()))

curChannel = 100

if not brokenBtn:
    print(N - M)
else:
    result = -1
    for i in range(len(N)):
        gap = 10
        cnt = 0
        nowBtn = 0
        for j in range(0, 11):
            if not j in brokenBtn:
                if gap > abs(int(N[i]) - j):
                    gap = abs(int(N[i]) - j)
                    nowBtn = j






    print(min((N - 100), result))