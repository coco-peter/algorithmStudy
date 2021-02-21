import sys

input = sys.stdin.readline

N, R = map(int, input().split())

child = 1
parent = 1

for i in range(N, N - (R - 1) - 1, -1):
    child *= i
    parent *= i - (N - (R - 1) - 1)


nCr = str(int(child / parent))

index = len(nCr) - 1
cnt = 0
while index > 0:
    # print(index, nCr[index])
    if nCr[index] != "0":
        break
    else:
        cnt += 1

    index -= 1
# print(nCr)
print(cnt)

