
N = int(input())
numList = [0] * 301
for i in range(N):
    numList[i] = (int(input()))

dp = [0] * 301
dp[0] = numList[0]
dp[1] = numList[1] + numList[0]
dp[2] = max(numList[1]+numList[2], numList[0]+numList[2])

for i in range(3,N):
    dp[i] = max(dp[i-2] + numList[i], dp[i-3] + numList[i-1] + numList[i])

print(dp[N-1])
