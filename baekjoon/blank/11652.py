
N = int(input())
numList = []
for i in range(N):
    numList.append(int(input()))

numList = sorted(numList)

cnt = 1
minIndex = numList[0]
maxValue = 1
for i in range(len(numList)-1):
    if numList[i] == numList[i+1]:
        cnt += 1
    else:
        cnt = 1
    if maxValue < cnt :
        maxValue = cnt
        minIndex = numList[i]

print(minIndex)