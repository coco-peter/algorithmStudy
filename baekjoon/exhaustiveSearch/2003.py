import sys

input = sys.stdin.readline

N, M = map(int,input().split())

numList = list(map(int, input().split()))

cnt = 0
for i in range(N):
    sumValue = 0
    for j in range(i, N):
        # tempList.append(numList[j])
        # print(sumValue)
        sumValue += numList[j]
        if sumValue == M:
            cnt += 1
        elif sumValue > M:
            break

print(cnt)