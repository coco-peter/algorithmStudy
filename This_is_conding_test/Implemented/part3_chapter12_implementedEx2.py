# 13 mintues

# K1KA5CB7
# AJKDLSI412K4JSJ9D

N = list(input())

word = []
sumNumber = 0
for i in N:
    if ord(i) >= 65:
        word.append(i)
    else:
        sumNumber += int(i)

word = sorted(word)

for i in word:
    print("%s"%i,end="")
print(sumNumber)

