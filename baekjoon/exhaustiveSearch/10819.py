from itertools import permutations

N = int(input())

numList = list(map(int,input().split()))

candidates = permutations(numList,N)

res = 0
for candidate in candidates:
    sumValue = 0
    for i in range(N-1):
        sumValue += abs(candidate[i] - candidate[i+1])

    res = max(res, sumValue)

print(res)