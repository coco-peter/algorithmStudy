# https://www.acmicpc.net/problem/1715

N = int(input())

candidates = [0] * N

for i in range(N):
    num = int(input())
    candidates[i] = num
candidates.sort()

sumValue = candidates[0]
sumValuelist = []
for i in range(1,N):
    num1, num2 = sumValue, candidates[i]
    sumValue = num1 + num2
    sumValuelist.append(sumValue)

print(sum(sumValuelist))


