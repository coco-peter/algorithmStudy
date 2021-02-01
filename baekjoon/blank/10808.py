#10m

word = list(input())
numList = [0] * 26
for i in range(len(word)):
    wordToNum = ord(word[i]) - 97
    numList[wordToNum] += 1

for i in numList:
    print("%d " %i, end="")
