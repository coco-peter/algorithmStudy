
N = int(input())
numList = list(map(int,input().split()))
dp = [0] * N

for i in range(N):
    for j in range(i):
        if numList[i] > numList[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1


if max(dp) == 1:
    print(len(numList))
else:
    maxIndex = -1
    for i in range(N):
        if dp[i] == max(dp):
            maxIndex = i
            break
    for j in range(maxIndex+1,N):
        for k in range(maxIndex, j):
            if numList[j] < numList[k] and dp[j] < dp[k]:
                dp[j] = dp[k]
        dp[j] += 1

    print(max(dp))
