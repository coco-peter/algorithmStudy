# https://www.acmicpc.net/problem/18353

N = int(input())

numList = list(map(int, input().split()))

numList.reverse()

Dp = [1] * N

for i in range(1,N):
    for j in range(0, i):
        if numList[j] < numList[i]:
            Dp[i] = max(Dp[i], Dp[j] + 1)


print(N - max(Dp))