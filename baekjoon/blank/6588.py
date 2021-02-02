import sys

input = sys.stdin.readline

numList = []
while True:

    N = int(input().strip())
    if N == 0:
        break
    numList.append(N)

max_num = max(numList)  # 와... max함수가 꽤나 시간을 잡아먹는구나 이것도 조심하자 !!!
prime = [False, False] + [True] * (max(numList)-1)
primeList = []
for i in range(2,max_num+1):
    if prime[i]:
        primeList.append(i)
        for j in range(i + i, max_num+1, i):
            prime[j] = False

for x in numList:
    for y in primeList:
        if prime[x-y] == 1:   # 요부분이 이해가 안감...
            print("%d = %d + %d" %(x, y, x-y))
            break


