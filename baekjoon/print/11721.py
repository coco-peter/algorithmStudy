
word = input()

for i in range(len(word)):
    if i % 10 == 0 and i != 0:
        print("")
    print(word[i], end="")