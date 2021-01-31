# 기존에 내 방법도 맞지 않나..??

N = int(input())

numList = list(map(int, input().split()))
dp = [0] * N

dp[0] = numList[0];

for i in range(N):
    temp = []
    for j in range(i):
        if numList[i] > numList[j]:
            temp.append(dp[j])
    if not temp:
        dp[i] = numList[i]
    else:
        dp[i] = max(temp) + numList[i]
print(dp)
print(max(dp))

