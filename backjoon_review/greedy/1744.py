import sys


input = sys.stdin.readline
numListplus = []
numListMinus = []
for _ in range(int(input())):
    num = int(input())
    if num > 0:
        numListplus.append(num)
    else:
        numListMinus.append(num)

numListplus = sorted(numListplus, reverse = True)
numListMinus = sorted(numListMinus)


result = []
i = 0

while i < len(numListplus):
    if i <= len(numListplus) -2:
        if numListplus[i] > 1 and numListplus[i+1] > 1:
            result.append(numListplus[i] * numListplus[i+1])
            i += 2
        elif numListplus[i] == 1 or numListplus[i+1] == 1:
            result.append(numListplus[i] + numListplus[i+1])
            i += 2
    else:
        result.append(numListplus[i])
        i += 1

i = 0
while i < len(numListMinus):
    if i <= len(numListMinus) -2:
        result.append(numListMinus[i] * numListMinus[i+1])
        i += 2
    else:
        result.append(numListMinus[i])
        i += 1

# print(result)
print(sum(result))