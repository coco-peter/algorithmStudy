# 거진 1h

N, K = map(int,input().split())

dp =[[0] * 201 for _ in range(201)]


for i in range(0,N+1):
    dp[1][i] = 1
for i in range(1,K+1):
    dp[i][0] = 1

for y in range(2,K+1):
    for x in range(1,N+1):
        dp[y][x] = dp[y-1][x] + dp[y][x-1]
        # print(y, x, dp[y][x], dp[y-1][x-1], dp[y][x-1])

print(dp[K][N] % 1000000000)
