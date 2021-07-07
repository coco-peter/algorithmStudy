import sys

input = sys.stdin.readline

word = list(input())
T = int(input())
cursur = len(word)

for _ in range(T):
    command = list(input().split())

    if command[0] == "L":
        if cursur == 0:
            continue
        cursur -= 1
    elif command[0] == "D":
        if cursur == len(word):
            continue
        cursur += 1
    elif command[0] == "B":

        if cursur == 0:
            continue
        del word[cursur-1]
        cursur -= 1
    elif command[0] == "P":

        word.insert(cursur,command[1])
        cursur += 1

for i in word:
    print(i,end="")
# print(word)