import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * 31

for i in range(2, N + 1, 2):
    if i == 2 :
        dp[i] = 3
    elif i == 4:
        dp[i] = dp[i-2] * 3 + 2
    else:
        dp[i] = dp[i - 2] * 3 + 2 + dp[i // 2] * 2

print(dp)
