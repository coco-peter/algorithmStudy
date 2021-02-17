import sys

input = sys.stdin.readline

N = int(input())

numList = [0]
for _ in range(N):
    numList.append(int(input()))

dp = [0] * (N + 1)

dp[1] = numList[1]

for i in range(2,N + 1):
    if i == 2:
        dp[2] = dp[1] + numList[2]
    else:
        dp[i] = max(dp[i-2] + numList[i] , dp[i-3] + numList[i-1] + numList[i])

# print(dp)
print(dp[N])