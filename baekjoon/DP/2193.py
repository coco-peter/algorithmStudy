#15m
# 이게 N이 1일 수도 있으니
# 배열은 항상 N의 최대치만큼 잡아놓고 시작하자 !!

N = int(input())

dp = [0] * (91)
dp[1] = 1
dp[2] = 1

for i in range(3,N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])