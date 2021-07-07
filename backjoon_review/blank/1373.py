# 1s 256MB

import sys

input = sys.stdin.readline

binaryList = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

num = input().strip()
# N , B = map(int,input().split())

def changeBtoN(B, N, res):
    index = 0
    for i in range(len(B) - 1, -1, -1):
        res += binaryList.find(B[i]) * pow(N, index)
        index += 1
        # print(B, N, B[i], binaryList.find(B[i]), pow(N, index), res)
    return res


def changeNtoB(N, B, res):
    # print(N, B, res)
    if N < B:
        res.append(binaryList[N])
        return res[::-1]

    res.append(binaryList[N % B])
    N = N // B

    return changeNtoB(N, B, res)

resultBtoN = changeBtoN(num, 2 , 0)
for i in changeNtoB(resultBtoN, 8, []):
    print(i, end="")

