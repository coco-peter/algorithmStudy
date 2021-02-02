import sys

input = sys.stdin.readline


# 조합
# nCk = n! / (k! * (n-k)!

# 와 진짜 개천재들..
def countNum(N,num):
    answer = 0
    while N != 0:
        N //= num
        answer += N

    return answer


N, M = map(int,input().split())

print(min((countNum(N,2) - countNum(M,2) - countNum(N-M,2)), (countNum(N,5)- countNum(M,5) - countNum(N-M,5))))