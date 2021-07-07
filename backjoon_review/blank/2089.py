


import sys
input = sys.stdin.readline

N = int(input())

if not N:
    sys.stdout.write('0')
    exit()
res = ""
while N:
    # print(N)
    if N % (-2):
        res = '1' + res
        # print(N, N // - 2, N // -2 +1)
        N = N //- 2 + 1
    else:
        res = '0' + res
        N //= -2

sys.stdout.write(res)


