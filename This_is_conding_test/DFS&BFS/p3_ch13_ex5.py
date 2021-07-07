# https://www.acmicpc.net/problem/14888

from itertools import permutations
import time

start = time.time()
N = int(input())

numberList = list(map(int, input().split()))
functionList = list(map(int, input().split()))

functionArray = []
for i in range(len(functionList)):
    for j in range(functionList[i]):
        if i == 0:
            functionArray.append("+")
        elif i == 1:
            functionArray.append("-")
        elif i == 2:
            functionArray.append("*")
        else:
            functionArray.append("//")


candidates = set(permutations(functionArray,len(functionArray)))

minValue = int(1e9)
maxValue = int(-1e9)

for candidate in candidates:
    result = numberList[0]
    for i in range(len(candidate)):
        if candidate[i] == "+":
            result += numberList[i+1]
        elif candidate[i] == "-":
            result -= numberList[i+1]
        elif candidate[i] == "*":
            result *= numberList[i+1]
        else:
            if result < 0:
                result = -result
                result //= numberList[i + 1]
                result = -result
            else:
                result //= numberList[i + 1]


    if minValue > result:
        minValue = result
    if maxValue < result:
        maxValue = result

print(maxValue)
print(minValue)
print("time: ", time.time() - start)