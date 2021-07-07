import sys
from itertools import permutations

# input = sys.stdin.readline

# 메모리 초과
# N = list(map(str,input().strip()))
#
# # candidateList = list(permutations(N, len(N)))
# #
# # max = -1
# # for candidate in candidateList:
# #     if candidate[0] == "0":
# #         continue
# #     sumValue = int("".join(candidate))
# #     if sumValue % 30 == 0 and max < sumValue:
# #         max = sumValue

# print(max)

N = input()
N = sorted(N, reverse = True)

sum = 0
if "0" not in N:
    print("-1")
else:
    for i in N:
        sum += int(i)
    if sum % 3 != 0:
        print(-1)
    else:
        print("".join(N))
