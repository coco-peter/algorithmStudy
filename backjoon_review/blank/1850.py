import sys

input = sys.stdin.readline

A, B = map(int, input().split())

def gcd(x,y):
    if y == 0:
        return x
    return gcd(y,x % y)


for i in range(gcd(A,B)):
    print("1", end="")
