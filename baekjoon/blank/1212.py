
import sys

input = sys.stdin.readline

N = input()

# print(oct(int(N,2)))
print(bin(int(N,8))[2:])
