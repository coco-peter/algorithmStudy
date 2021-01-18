# https://www.acmicpc.net/problem/18353

N = int(input())

numList = list(map(int, input().split()))

count = 0
for i in range(N-1,1,-1):

    if numList[i] > numList[i-1]:
        if numList[i] <= numList[i-2]:
            del numList[i-1]
            count += 1
        else:
            del numList[i]
            count += 1
    else:
        if numList[i] > numList[i - 2]:
            del numList[i-2]
            count += 1

# print(numList)
print(count)
