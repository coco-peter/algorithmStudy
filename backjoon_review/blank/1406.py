# 0.3s 512MB

import sys

input = sys.stdin.readline

word = list(map(str,input().rstrip()))

cursor = len(word)
for _ in range(int(input())):
    command = list(map(str,input().split()))

    if command[0] == "L":
      if cursor == 0:
          continue
      else:
          cursor -= 1
    elif command[0] == "D":
        if cursor == len(word):
            continue
        else:
            cursor += 1
    elif command[0] == "B":
        if cursor == 0:
            continue
        else:
            del word[cursor -1]
        cursor -= 1
    elif command[0] == "P":
        word.insert(cursor, command[1])
        cursor += 1

for i in word:
    print(i, end = "")