#20ms

N = int(input())
numList = list(map(int,input().split()))
dp = [0] * N
dp[0] = numList[0]

for i in range(1,N):
    if dp[i-1] < 0:
        dp[i] = numList[i]
    else:
        dp[i] = numList[i] + dp[i-1]

print(dp)
print(max(dp))