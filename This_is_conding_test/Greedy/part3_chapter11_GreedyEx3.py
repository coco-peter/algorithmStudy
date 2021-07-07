# 30 minutes
# 틀림 왜 틀렸지...??
# 아하... 너무 깊게 생각했다..
# 다음에 다시 풀기 !

S = list(input())

zeroPairCount = 0
onePairCount = 0
isfirst = 0
nowNum = "-1"
for i in S:

    if isfirst == 0:
        nowNum = i
        isfirst = 1
        if nowNum == '0':
            zeroPairCount += 1
        else:
            onePairCount += 1
        continue

    if i == '0' and nowNum == i:            # 0 0
        continue
    elif i == '0' and nowNum != i:          # 1 0
        zeroPairCount += 1
    elif i == '1' and nowNum == i:          # 1 1
        continue
    elif i == '1' and nowNum != i:          # 0 1
        onePairCount += 1
    nowNum = i
    # print(nowNum)

if zeroPairCount >= onePairCount:
    if onePairCount == 0:
        print(zeroPairCount)
    else:
        print(onePairCount)
elif onePairCount >= zeroPairCount:
    if zeroPairCount == 0:
        print(onePairCount)
    else:
        print(zeroPairCount)


# print(min(zeroPairCount,onePairCount))

