import sys

input = sys.stdin.readline

N, M, K = map(int,input().split())

while K != 0:
    if N > M * 2:

        N -= 1
        K -= 1
    else:

        M -= 1
        K -= 1

cnt = 0
while True:
    # print(N, M)
    if N - 2 >= 0 and M - 1 >= 0:
        N -= 2
        M -= 1
        cnt += 1
    else:
        break
print(cnt)