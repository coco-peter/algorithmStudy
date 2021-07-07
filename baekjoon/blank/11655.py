
while True:
    try:
        word = list(input())
        lockedWord = ""
        # print(word)
        for i in range(len(word)):
            if word[i] == " ":
                lockedWord += (word[i])
            elif ord(word[i]) >= 97 and ord(word[i]) <= 122:
                changedNum = ord(word[i]) + 13
                if changedNum >= 123:
                    changedNum = changedNum - 26
                lockedWord += (chr(changedNum))
            elif ord(word[i]) >= 65 and ord(word[i]) <= 90:
                changedNum = ord(word[i]) + 13
                if changedNum >= 91:
                    changedNum = changedNum - 26
                lockedWord+= (chr(changedNum))
            elif ord(word[i]) >= 48 and ord(word[i]) <= 57:
                lockedWord+= (word[i])

        print(lockedWord)

    except:
        break

