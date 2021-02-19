#1s 128MB


import sys
# import math

input = sys.stdin.readline

binaryList = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

B, N = map(str, input().split())
result = 0
def changeBtoN(B, N, res):
    index = 0
    for i in range(len(B) - 1, -1, -1):
        # print(B, N, binaryList.find(B[i]), pow(N, index))
        res += binaryList.find(B[i]) * pow(N, index)
        index += 1
    return res


print(changeBtoN(B, int(N), result))