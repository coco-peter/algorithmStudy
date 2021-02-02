
import sys

input = sys.stdin.readline

N, B = map(int,input().split())

numList = "01"
res = ""
while N != 0:
    res += numList[N % B]
    N //= B

print(res[::-1])
