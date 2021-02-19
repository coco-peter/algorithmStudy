# 1s 256MB

import sys

input = sys.stdin.readline

binaryList = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N , B = map(int,input().split())
def calBinary(N, B, res):
    # print(N, B, res)
    if N < B:
        res.append(binaryList[N])
        return res

    res.append(binaryList[N % B])
    N = N // B

    return calBinary(N, B, res)


result = calBinary(N, B, [])

for i in range(len(result) -1, -1, -1):
    print(result[i], end="")