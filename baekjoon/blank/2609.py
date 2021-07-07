import sys

input = sys.stdin.readline

A, B = map(int, input().split())

def gcd(x,y):
    if y == 0:
        return x
    return gcd(y,x % y)

def lcm(x,y):
    return x * y // gcd(x,y)


print(gcd(A,B))
print(lcm(A,B))