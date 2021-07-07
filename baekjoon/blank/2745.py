
import sys

input = sys.stdin.readline

N, B = input().split()

numList = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = ""
num = 0
cnt = 0

for i in range(len(N)-1, -1, -1):
    res = (int(B) ** cnt) * numList.index(N[i])
    num += res
    cnt += 1

print(num)
