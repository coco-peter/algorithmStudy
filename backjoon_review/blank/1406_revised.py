import sys

input = sys.stdin.readline

word1 = list(input().strip())
word2 = []
n = int(input())
for _ in range(n):
    command = list(map(str, input().split()))
    if command[0] == "L":
        if word1:
            word2.append(word1.pop())
        else:
            continue
    elif command[0] == "D":
        if word2:
            word1.append(word2.pop())
        else:
            continue
    elif command[0] == "B":
        if word1:
            word1.pop()
        else:
            continue
    elif command[0] == "P":
        word1.append(command[1])

print("".join(word1 + list(reversed(word2))))