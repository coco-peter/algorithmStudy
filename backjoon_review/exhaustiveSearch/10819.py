import sys

input = sys.stdin.readline

N = int(input())

numList = list(map(int, input().split()))
numList = sorted(numList)

if len(numList) % 2 == 0:
    smallList = sorted(numList[:len(numList)//2], key= lambda x : (abs(x)), reverse = True)
    bigList = sorted(numList[len(numList)//2:], reverse = True)
else:
    smallList = sorted(numList[:len(numList)//2 + 1], key= lambda x : (abs(x)), reverse = True)
    bigList = sorted(numList[len(numList) // 2 + 1:], reverse=True)

# print(smallList, bigList)
smallIndex = 0
bigIndex = 0
newList = []
while smallIndex < len(smallList) or bigIndex < len(bigList):
    if smallIndex < len(smallList):
        newList.append(smallList[smallIndex])
        smallIndex += 1
    if bigIndex < len(bigList):
        newList.append(bigList[bigIndex])
        bigIndex += 1

# print(newList)
cnt = 0
for i in range(N - 1):
    cnt += abs(newList[i] - newList[i+1])
print(cnt)