# 9m


N = int(input())

dp = [0] * (N+1)

dp[1] = 0
INF = int(1e9)
for i in range(2,N+1):
    cost = INF
    if i % 2 == 0:
        cost = min(cost, dp[i // 2] + 1)
    if i % 3 == 0:
        cost = min(cost, dp[i // 3] + 1)

    cost = min(cost, dp[i-1] + 1)
    dp[i] = cost

print(dp[N])
