

while True:
    try:
        word = list(input())
        bigWord = 0
        smallWord = 0
        number = 0
        space = 0
        # print(word)
        for i in range(len(word)):
            if word[i] == " ":
                space += 1
            elif ord(word[i]) >= 97 and ord(word[i]) <= 122:
                smallWord += 1
            elif ord(word[i]) >= 65 and ord(word[i]) <= 90:
                bigWord += 1
            elif ord(word[i]) >= 48 and ord(word[i]) <= 57:
                number += 1

        print("%d %d %d %d" %(smallWord,bigWord,number,space))

    except:
        break

