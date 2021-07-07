import sys

input = sys.stdin.readline

for T in range(int(input())):
    N = int(input())
    dp = [[0] * N for _ in range(2)]
    numList = [[0] * N for _ in range(2)]

    for y in range(2):
        inputList = list(map(int,input().split()))
        for x in range(N):
            numList[y][x] = inputList[x]

    # print(numList)
    dp[0][0], dp[1][0] = numList[0][0], numList[1][0]
    for x in range(1, N):
        for y in range(2):
            if x == 1 and y % 2 == 0:
                dp[y][x] = dp[y + 1][x-1] + numList[y][x]
            elif x == 1 and y % 2 == 1:
                dp[y][x] = dp[y - 1][x - 1] + numList[y][x]
            elif y % 2 == 0:
                dp[y][x] = max(dp[y + 1][x - 1] + numList[y][x], dp[y + 1][x-2] + numList[y][x])
            elif y % 2 == 1:
                dp[y][x] = max(dp[y - 1][x - 1] + numList[y][x], dp[y - 1][x-2] + numList[y][x])

    print(max(dp[0][N-1], dp[1][N-1]))
