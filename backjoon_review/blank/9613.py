# 1s 128MB

import sys
from itertools import combinations

input = sys.stdin.readline

def GCD(x, y):
    if y == 0:
        return x
    return GCD(y, x % y)

for t in range(int(input())):

    numList = list(map(int, input().split()))
    candidates = combinations(numList[1:], 2)

    sumValue = 0
    for candidate in candidates:
        # print(candidate[0], candidate[1])
        res = GCD(candidate[0], candidate[1])
        sumValue += res

    print(sumValue)