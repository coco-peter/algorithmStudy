import sys

input = sys.stdin.readline

N = int(input())

prime = [False, False] + [True] * (N-1)
primeList = []

for i in range(2,N+1):
    if prime[i]:
        primeList.append(i)
        for j in range(i+i, N+1, i):
            prime[j] = False

# print(primeList)
resultList = []
while N != 1:
    for i in primeList:
        if N % i == 0:
            resultList.append(i)
            N //= i
            break

resultList = sorted(resultList)

for i in resultList:
    print(i)