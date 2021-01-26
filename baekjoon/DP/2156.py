# maybe 40~50m


N = int(input())

numList = [0]


for _ in range(N):
    numList.append(int(input()))

dp = [0] * (10001)
dp[1] = numList[1]

for i in range(2,N+1):
    if i == 2:
        dp[i] = dp[i-1] + numList[i]
    dp[i] = max(dp[i-1], numList[i] + dp[i-2], numList[i] + numList[i-1] + dp[i-3])

print(dp[N])
