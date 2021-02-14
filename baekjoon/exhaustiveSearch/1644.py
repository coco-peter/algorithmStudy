import sys

input = sys.stdin.readline

N = int(input())

numArray = [True] * 4000001

for i in range(2,len(numArray) // 2):
    if numArray[i] == 0:
        for j in range(i + i, len(numArray) ,i):
            numArray[j] = False

primeList = []
for i in range(2,len(numArray)):
    if numArray[i] == True:
        primeList.append(i)



