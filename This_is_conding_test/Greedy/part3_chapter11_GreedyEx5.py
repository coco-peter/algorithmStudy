# 5 3
# 1 3 2 3 2
#
# 8 5
# 1 5 4 3 2 4 5 2

# 7 minutes

N, M = map(int, input().split())

kgBalls = list(map(int, input().split()))

cntPairBalls = 0

for i in range(0, len(kgBalls)):
    for j in range(i+1, len(kgBalls)):
        if kgBalls[i] != kgBalls[j]:
            cntPairBalls += 1


print(cntPairBalls)
