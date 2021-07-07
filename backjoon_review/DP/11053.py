import sys

input = sys.stdin.readline

N = int(input())

numList = [0] + list(map(int,input().split()))
dp = [0] * (N + 1)
dp[0] = 1

for i in range(2, N + 1):
    cnt = 0
    isVisited = [0] * 1001
    temp = 0
    for j in range(1, i):
        if numList[i] > numList[j] and temp < numList[j]:
            temp = numList[j]
            cnt += 1
    if cnt > 0:
        dp[i] = cnt + 1

# print(dp)
print(max(dp))