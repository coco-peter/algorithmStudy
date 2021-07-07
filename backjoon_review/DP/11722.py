import sys

input = sys.stdin.readline

N = int(input())

numList = list(map(int,input().split()))

dp = [0] * N

for i in range(N):
    for j in range(i):
        if numList[i] < numList[j]:
            dp[i] = max(dp[i], dp[j])

    dp[i] += 1

# print(dp)
print(max(dp))