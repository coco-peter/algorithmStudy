# 5 3
# 1 2 5 4 3
# 5 5 6 6 5

N, K = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b, reverse = True)

for i in range(K):
        if a[i] < b[i]:
                a[i], b[i] = b[i], a[i]

print(sum(a))