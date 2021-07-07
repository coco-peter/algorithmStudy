import sys

input = sys.stdin.readline

N = int(input())

numList = []

for _ in range(N):
    numList.append(int(input()))

numList = sorted(numList)
# print(numList)
isPaired = False
res = 0
for i in range(len(numList)-1, -1, -1):
    # print(numList[i], res)
    if isPaired == False:
        if numList[i] * numList[i-1] > numList[i] + numList[i-1] and i > 0:
            res += numList[i] * numList[i-1]
            isPaired = True
        else:
            res += numList[i]
    else:
        isPaired = False
        continue

print(res)
