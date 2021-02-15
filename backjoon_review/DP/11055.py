import sys

input = sys.stdin.readline

N = int(input())

numList = list(map(int,input().split()))
dp = [0] * (N)
dp[0] = numList[0]

for i in range(1, N):
    temp = 0
    for j in range(0, i):
        if numList[i] > numList[j] and temp < numList[j]:
            temp = numList[j]
            dp[i] += numList[j]

    dp[i] += numList[i]

print(dp)
print(max(dp))