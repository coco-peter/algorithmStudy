# 다시 풀어보자...

# aabbaccc



word = list(input())

sameWordCount = 1
isSameWord = -1
sameWordList = []
print(int(len(word)/2))
for i in range(1,int(len(word)/2)):             # 몇 쌍까지 조사할 것인지?
    for j in range(0,len(word) - i):            # 첫번째 자리 부터 몇 번째 자리까지 검사??
        for k in range(0,i):                    # i 쌍에서 만약 i가 1이면 바로 뒤에 있는것만 검사하면 됨. j 자리에서
            # print(word[j], word[j+i])
            if sameWordCount < i + 1:
                sameWordList.append(word[j])
            if word[j] == word[j+i]:
                isSameWord = 1
                # print("sameword")
                # if sameWordCount < i + 1:
                #     print("sameword")
                #     sameWordList.append(word[j])
            if word[j] != word[j+i]:
                # print("diff")
                isSameWord = 0
                # sameWordList.clear()


        if isSameWord == 1:
            sameWordCount += 1
            if j == len(word) - i - 1:
                isSameWord = 0

        if isSameWord == 0:
            if sameWordCount > 1:
                print("%d"%sameWordCount, end="")
            for sameWord in sameWordList:
                print(sameWord,end="")
            sameWordCount = 1
            sameWordList.clear()

    print("")


