import sys
from itertools import combinations

input = sys.stdin.readline

A = int(input())

def gcd(x,y):
    if y == 0:
        return x
    return gcd(y,x % y)

for _ in range(A):
    numList = list(map(int, input().split()))
    numList = numList[1:]
    res = 0
    for a, b in combinations(numList,2):
        res += gcd(a,b)
    print(res)

