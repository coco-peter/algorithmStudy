import sys

input = sys.stdin.readline

N = int(input())

numList = list(map(int, input().split()))


res = 0
for k in numList:
    cnt = 0
    if k == 1:
        continue
    for i in range(2,k+1):
        if k % i == 0:
            cnt += 1

    if cnt == 1:
        res += 1

print(res)


