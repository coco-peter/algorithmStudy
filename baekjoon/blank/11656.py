
word = input()

wordList = []

for i in range(0,len(word)):
    wordList.append(word[i:])

wordList = sorted(wordList)
for i in wordList:
    print(i)

