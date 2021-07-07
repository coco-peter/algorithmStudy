import sys
from itertools import combinations

while True:
    inputList = list(map(int, input().split()))
    if inputList[0] == 0:
        break

    K = inputList[0]
    S = inputList[1:]

    candidates = combinations(S,6)
    for candidate in candidates:
        for i in candidate:
            print(i, end =" ")
        print("")

    print("")
