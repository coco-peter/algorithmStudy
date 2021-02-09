import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

possibleBtn = []

if M != 0:
    impossibleBtn = list(map(str,input().split()))
else:
    impossibleBtn = []

minCnt = abs(100 - N)

# 브루트 포스...?? : 모든 경우의 수를 수행한다??
# 시간초과가 안걸리네??
for num in range(1000001):
    num = str(num)
    for j in range(len(num)):
        if num[j] in impossibleBtn:
            break
        elif j == len(num) - 1:
            minCnt = min(minCnt, abs(N - int(num)) + len(str(num)))

print(minCnt)



