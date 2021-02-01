import sys

input = sys.stdin.readline

N = int(input())

def gcd(x,y):
    if y == 0:
        return x
    return gcd(y,x % y)

def lcm(x,y):
    return x * y // gcd(x,y)

for _ in range(N):
    A, B = map(int, input().split())
    print(lcm(A,B))


