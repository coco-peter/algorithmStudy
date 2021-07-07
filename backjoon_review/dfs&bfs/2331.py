import sys


input = sys.stdin.readline

A, P = map(int,input().split())

numList = [str(A)]
nowNum = str(A)


# cnt = 1
index = -1
while True:

    sumValue = 0
    # print(numList)
    for i in range(len(nowNum)):
        sumValue += int(nowNum[i]) ** P

    if str(sumValue) in numList:
        index = numList.index(str(sumValue))
        break
    else:
        numList.append(str(sumValue))
        nowNum = str(sumValue)
        # cnt += 1

print(index)