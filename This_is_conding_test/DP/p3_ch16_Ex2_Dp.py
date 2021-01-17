n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))

# print(dp)
for y in range(1,n):
    for x in range(y+1):
        # 왼쪽 위
        if x == 0:
            left_top = 0
        else:
            left_top = dp[y-1][x-1]

        # 바로 위
        if x == y:
            top = 0
        else:
            top = dp[y-1][x]

        dp[y][x] = dp[y][x] + max(left_top, top)

result = 0
for x in range(n):
    result = max(result, dp[n-1][x])

print(result)