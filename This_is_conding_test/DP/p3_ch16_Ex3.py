# https://www.acmicpc.net/problem/14501

N = int(input())
t = []
p = []
dp = [0] * (N+1)

for _ in range(N):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

max_value = 0
for i in range(N-1,-1,-1):
    time = i + t[i]
    if time > N:
        dp[i] = max_value
    else:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]

print(max_value)