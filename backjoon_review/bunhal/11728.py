import sys

input = sys.stdin.readline

N, M = map(int,input().split())

firstList = list(map(int,input().split()))
secondList = list(map(int,input().split()))

firstIndex = 0
secondIndex = 0

sortedList = []
while True:
    if firstIndex == len(firstList):
        sortedList += secondList[secondIndex:]
        break
    elif secondIndex == len(secondList):
        sortedList += firstList[firstIndex:]
        break

    if firstList[firstIndex] <= secondList[secondIndex]:
        sortedList.append(firstList[firstIndex])
        firstIndex += 1
    else:
        sortedList.append(secondList[secondIndex])
        secondIndex += 1

for i in sortedList:
    print(i, end = " ")