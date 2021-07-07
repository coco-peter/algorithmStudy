# 아직 멀었다..

# 2 15
# 2
# 3

# 3 4
# 3
# 5
# 7

N, M = map(int, input().split())
moneyList = []
for i in range(N):
    moneyList.append(int(input()))

dp = [10001] * (M + 1)
dp[0] = 0



for i in range(N):
    for j in range(moneyList[i], M+1):
        if dp[j - moneyList[i]] != 10001:
            dp[j] = min(dp[j], dp[j-moneyList[i]] + 1)

if dp[M] == 10001:
    print("-1")
else:
    print(dp[M])

