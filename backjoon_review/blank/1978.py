import sys

input = sys.stdin.readline

primeNum = [False] * 1000001
primeNum[0] = primeNum[1] = True
for i in range(2, len(primeNum) // 2):
    for j in range(i + i , len(primeNum), i):
        if primeNum[j] == False:
            primeNum[j] = True

M, N  = map(int,input().split())

cnt = 0
for i in range(M, N + 1):
    if primeNum[i] == False:
        print(i)
