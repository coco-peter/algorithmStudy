import sys

input = sys.stdin.readline

N, K = map(int,input().split())

moneyList = []

for _ in range(N):
    moneyList.append(int(input()))

cnt = 0
while K != 0:
    for i in range(len(moneyList)-1, -1, -1):
        if K - moneyList[i] >= 0:
            cnt += 1
            K = K - moneyList[i]
            break

print(cnt)