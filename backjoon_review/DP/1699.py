import sys
import math

input = sys.stdin.readline

N = int(input())
dp = [0] * ( N + 1)


for i in range(1, N + 1):
    temp = i
    tempSqrt = int(math.sqrt(temp))
    tempPow = pow(tempSqrt, 2)
    temp -= tempPow
    dp[i] = dp[temp] + 1

print(dp)
print(dp[N])
