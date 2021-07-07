# 못품 ...

N = int(input())

dp = [[0] * 10 for _ in range(101)]
for i in range(10):
    dp[1][i] = 1

for y in range(1,100):
    for x in range(10):
        if x > 0:
            dp[y+1][x-1] += dp[y][x]
        if x < 9:
            dp[y+1][x+1] += dp[y][x]

print(dp)
print((sum(dp[N][:]) - dp[N][0]) % 1000000000 )




