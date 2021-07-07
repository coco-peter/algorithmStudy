import sys
from itertools import combinations
input = sys.stdin.readline


N, S = map(int,input().split())

numList = list(map(int,input().split()))
cnt = 0


for i in range(1,N+1):
    candidates = combinations(numList,i)
    for candidate in candidates:
        if sum(candidate) == S:
            # print(candidate)
            cnt += 1

print(cnt)