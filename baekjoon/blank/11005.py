
import sys

input = sys.stdin.readline

N, B = map(int,input().split())

numList = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = ""
while N != 0:
    res += numList[N % B]
    N //= B

print(res[::-1])
