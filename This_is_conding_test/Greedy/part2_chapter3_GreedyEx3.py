# ex3
# 15 minutes


N, K = map(int, input().split())

count = 0
while True:

    if N % K == 0:
        N = N / K
        count = count + 1
    else:
        N = N - 1
        count = count + 1

    if N == 1:
        break

print(count)

# N = N / K -- > N //= K
# N = N + 1 --> N += 1