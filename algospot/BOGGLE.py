import sys
from collections import deque

input = sys.stdin.readline


dx = [0, 0, 1, -1, -1, 1, -1, 1]
dy = [1, -1, 0, 0, -1, 1, 1, -1]

def isThereWord(x, y, index):
    global wordCheck, wordMap, checkWord

    wordCheck[y][x][index] = 1
    if wordMap[y][x] != checkWord[index]:
        return False

    if index == len(checkWord) - 1:
        return True

    index += 1
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            if wordCheck[ny][nx][index]:
                continue
            if isThereWord(nx, ny, index):
                return True




for t in range(int(input())):
    wordMap = [[0] * 5 for _ in range(5)]
    wordCheck = [[[0] * 10 for _ in range(5)] for _ in range(5)]

    # print(wordCheck)

    for y in range(5):
        wordList = list(map(str,input().strip()))
        for x in range(5):
            wordMap[y][x] = wordList[x]

    # print(wordMap)


    for i in range(int(input())):
        wordCheck = [[[0] * 10 for _ in range(5)] for _ in range(5)]
        checkWord = input().strip()
        isThere = False
        for y in range(5):
            for x in range(5):
                if isThereWord(x, y, 0):
                    isThere = True
                if isThere:
                    break

            if isThere:
                break

        if isThere:
            print(checkWord, "YES")
        else:
            print(checkWord, "NO")

        # print(checkWord, isThereWord(wordMap, checkWord, len(checkWord), 0))