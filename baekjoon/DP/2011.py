N = list(map(int, input()))
length = len(N)
dp = [0] * (len(N) + 1)

if N[0] == 0:
    print(0)
else:
    N = [0] + N
    dp[0] = 1
    dp[1] = 1
    for i in range(2, len(N)):
        cur = int(N[i])
        cur2 = int(N[i]) + int(N[i-1]) * 10

        if 1 <= cur <= 9:
            dp[i] += dp[i-1]
        if 10 <= cur2 <= 26:
            dp[i] += dp[i-2]
        dp[i] %= 1000000

    print(dp[length])