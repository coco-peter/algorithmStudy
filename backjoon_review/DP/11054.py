import sys

input = sys.stdin.readline

N = int(input())

numList = list(map(int,input().split()))

increaseDp = [1] * N
decreaseDp = [1] * N
resDp = [0] * N

for i in range(N):
    for j in range(i):
        if numList[i] > numList[j]:
            increaseDp[i] = max(increaseDp[i], increaseDp[j] + 1)

for i in range(N-1, -1, -1):
    for j in range(i, N):
        if numList[i] > numList[j]:
            decreaseDp[i] = max(decreaseDp[i], decreaseDp[j] + 1)

    resDp[i] = increaseDp[i] + decreaseDp[i] - 1


print("증가하는 부분수열 " + str(increaseDp))
print("감소하는 부분수열 " + str(decreaseDp))
print("바이토닉 부분수열 " + str(resDp))
print(max(resDp))
