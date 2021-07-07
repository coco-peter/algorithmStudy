import sys

input = sys.stdin.readline

primeNum = [False] * 1000001
primeNum[0] = primeNum[1] = True
for i in range(2, len(primeNum) // 2):
    for j in range(i + i , len(primeNum), i):
        if primeNum[j] == False:
            primeNum[j] = True

while True:
    N = int(input())
    if N == 0:
        break

    a = 3
    b = N - 1
    isPossible = False
    while a <= b:
        # print(a, b, a + b)
        if a + b == N:
            if primeNum[b] == False and primeNum[a] == False:
                isPossible = True
                print("%d = %d + %d"%(N, a, b))
                break
            elif primeNum[b] == True:
                while primeNum[b] == True:
                    b -= 2
            elif primeNum[a] == True:
                while primeNum[a] == True:
                    a += 2
        elif a + b > N:
            b -= 2
            while primeNum[b] == True:
                b -= 2
        elif a + b < N:
            a += 2
            while primeNum[a] == True:
                a += 2


    if isPossible == False:
        print("Goldbach's conjecture is wrong.")
