import sys

input = sys.stdin.readline

N = int(input())
cardList = list(map(int,input().split()))

M = int(input())
checkList = list(map(int,input().split()))

# 딕셔너리 문법에 대해 한번 공부해보자...
cardListCnt = {}
for i in cardList:
    try:
        cardListCnt[i] += 1
    except:
        cardListCnt[i] = 1

print(cardListCnt)


res = []
for i in checkList:
    try:
        res.append((cardListCnt[i]))
    except:
        res.append(0)

for i in res:
    print(i, end = ' ')

