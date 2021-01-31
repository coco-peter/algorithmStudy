N = int(input())
numList = []
for i in range(N):
    numList.append(int(input()))

numList = sorted(numList)

for i in range(N):
    print(numList[i])